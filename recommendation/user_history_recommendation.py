import re
import pymongo
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer


class ProductRecommender:
    def __init__(self, mongo_uri, db_name, product_type, n_neighbors=3):
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.products_collection = self.db[product_type]  
        self.n_neighbors = n_neighbors
        self.vectorizer = TfidfVectorizer()  

    @staticmethod
    def parse_price(price_str):
        price_str = price_str.replace('\n', '').replace('$', '').strip()
        try:
            return float(price_str)
        except ValueError:
            return 0.0

    @staticmethod
    def extract_keywords(description):
        keywords = re.findall(r'\b\w+\b', description.lower())
        return set(keywords)

    @staticmethod
    def calculate_env_index(description):
        eco_keywords = {
            "organic": 2,
            "bamboo": 3,
            "recycled": 2,
            "sustainable": 2,
            "eco-friendly": 3,
            "natural": 1
        }
        description_keywords = set(description.lower().split())
        env_score = sum(eco_keywords.get(word, 0) for word in description_keywords)
        return min(env_score, 5)

    def ensure_env_index(self, product):
        if 'env-index' not in product or product['env-index'] == 0:
            product['env-index'] = self.calculate_env_index(product['description'])
        return product

    def vectorize_products(self, products):
        descriptions = [' '.join(self.extract_keywords(product['description'])) for product in products]
        tfidf_matrix = self.vectorizer.fit_transform(descriptions) 
        numeric_features = np.array([[self.parse_price(product['price']),
                                      product.get('env-index', 0)]
                                     for product in products])

        numeric_features = np.nan_to_num(numeric_features, nan=0.0)

        return np.hstack((tfidf_matrix.toarray(), numeric_features))

    def transform_user_history(self, user_history):
        """Transform user history descriptions using the existing vectorizer."""
        descriptions = [' '.join(self.extract_keywords(product['description'])) for product in user_history]
        tfidf_matrix = self.vectorizer.transform(descriptions)
        numeric_features = np.array([[self.parse_price(product['price']),
                                      product.get('env-index', 0)]
                                     for product in user_history])

        numeric_features = np.nan_to_num(numeric_features, nan=0.0)

        return np.hstack((tfidf_matrix.toarray(), numeric_features))

    def recommend_knn_based(self, user_history):
        """Recommend products based on the user's history using KNN."""
        user_history = [self.ensure_env_index(product) for product in user_history]

        all_products = list(self.products_collection.find())
        all_products = [self.ensure_env_index(product) for product in all_products]
        all_product_vectors = self.vectorize_products(all_products)
        history_vectors = self.transform_user_history(user_history)

        knn = NearestNeighbors(n_neighbors=self.n_neighbors, metric='cosine')
        knn.fit(all_product_vectors)

        distances, indices = knn.kneighbors(history_vectors)
        indices = np.unique(indices.flatten())
        return [all_products[i] for i in indices]

    def get_user_history(self, limit=3):
        """Fetch the last n items from user-history."""
        user_history = list(self.db['user-history'].find().sort('_id', -1).limit(limit))
        return user_history if user_history else []

    def update_user_history(self, cases):
        for case in cases:
            try:
                self.db['user-history'].insert_one(case)
            except pymongo.errors.DuplicateKeyError:
                print(f"Duplicate entry found for: {case['_id']}, skipping insertion.")


if __name__ == "__main__":
    mongo_uri = 'mongodb+srv://hibaaltaf98:HotChocolate333!@cluster0.eokpf.mongodb.net/'
    db_name = 'sustainable-products-1'
    product_type = 'shirt'
    recommender = ProductRecommender(mongo_uri, db_name, product_type)
    user_history = recommender.get_user_history()  
    if not user_history:
        print("No user history found. Cannot generate recommendations.")
    else:
        recommended_products_knn = recommender.recommend_knn_based(user_history)
        print("\n-- K-NN-based Recommendations: --\n")
        for record in recommended_products_knn:
            print(record)
            print('\n')


