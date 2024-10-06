import re
import pymongo
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import os
from dotenv import load_dotenv
from update_sustainability import SustainabilityCalculator

load_dotenv()

class ProductRecommender:
    def __init__(self, mongo_uri, db_name, user_case):
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.user_case = user_case
        self.products_collection = self.db[user_case['type']]  


    @staticmethod
    def parse_price(price_str):
        price_str = price_str.replace('\n', '').replace('$', '').strip()
        try:
            return float(price_str)
        except ValueError:
            return 0.0  #

    @staticmethod
    def extract_keywords(description):
        keywords = re.findall(r'\b\w+\b', description.lower())
        return set(keywords)

    def vectorize_products(self, products):
        vectorizer = TfidfVectorizer()
        descriptions = [' '.join(self.extract_keywords(product['description'])) for product in products]
        tfidf_matrix = vectorizer.fit_transform(descriptions)

        numeric_features = np.array([[self.parse_price(product['price']),
                                      product.get('env-index', 0)]  
                                     for product in products])

        numeric_features = np.nan_to_num(numeric_features, nan=0.0)

        return np.hstack((tfidf_matrix.toarray(), numeric_features))


    def recommend_ml_based(self, user_selected_products):
        all_products = user_selected_products + [self.user_case] 
        product_vectors = self.vectorize_products(all_products)

        similarity_matrix = cosine_similarity(product_vectors)
        user_similarities = similarity_matrix[0, 1:]
        recommendations = np.argsort(-user_similarities)
        all_products_list = list(self.products_collection.find())
        return [all_products_list[i] for i in recommendations[:3]]


    def recommend_similar_products(self):
        current_score = self.user_case.get('env-index', 0)
        current_price = self.parse_price(self.user_case['price'])
        current_keywords = self.extract_keywords(self.user_case['description'])

        recommendations = []

        for product in self.products_collection.find():
            product_score = product.get('env-index', 0)
            product_price = self.parse_price(product['price'])
            product_keywords = self.extract_keywords(product['description'])
            if product_score >= current_score - 2 and product_score > current_score and abs(product_price - current_price) <= 15:
                keyword_match_count = len(current_keywords.intersection(product_keywords))
                recommendations.append((product, keyword_match_count))

        recommendations.sort(key=lambda x: (-x[1], x[0]['price']))
        return [r[0] for r in recommendations[:3]]
    
    # def update_user_history(self,cases):
    #     self.db['user-history'].insert_many(cases)

    def update_user_history(self, cases):
        for case in cases:
            try:
                self.db['user-history'].insert_one(case)
            except pymongo.errors.DuplicateKeyError:
                print(f"Duplicate entry found for: {case['_id']}, skipping insertion.")

if __name__ == "__main__":
    print("\n---Item You Wish to Buy: ---\n")

    user_case = {
        "product_details": "90% bamboo, 10% organic cotton",
        "price": "65",
        "description": "Red cotton t-shirt medium",
        "brand": "Quince",
        "color": "Red",
        "url": "https://quince.com/women/apparel/top/bamboo-cotton",
        "image": "https://quince.com/images/top18.jpg",
        "type": "shirt"  
    }

    recommender = ProductRecommender(os.getenv("MONGODB_URI"), os.getenv("DB_NAME"), user_case)
    products = list(recommender.products_collection.find())
    recommended_products_ml = recommender.recommend_ml_based(products)
    print("\n-- ML-based Recommendations: --\n")
    for case in recommended_products_ml:
        print(case)
        print('\n')

    similar_recommended_products = recommender.recommend_similar_products()
    print("\n-- Sustainability Recommendations: --\n")
    for case in similar_recommended_products:
        print(case) 
        print('\n')


    user_history_cases = [user_case]
    user_history_cases.extend(recommended_products_ml)
    recommender.update_user_history(user_history_cases)