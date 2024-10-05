import re
import pymongo
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]  # replace with your database name
products_collection = db["products"]  # replace with your collection name


# Function to parse price into a float
def parse_price(price_str):
    price_str = price_str.replace('\n', '').replace('$', '').strip()
    try:
        return float(price_str)
    except ValueError:
        return 0.0  # Return 0 if parsing fails


# Function to extract keywords from description for similarity matching
def extract_keywords(description):
    keywords = re.findall(r'\b\w+\b', description.lower())
    return set(keywords)


# Function to vectorize products for content-based filtering
def vectorize_products(products):
    vectorizer = TfidfVectorizer()

    descriptions = [' '.join(extract_keywords(product['description'])) for product in products]
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    numeric_features = np.array([[parse_price(product['price']),
                                  product['sustainability_score']]
                                 for product in products])

    # Replace NaN values with 0
    numeric_features = np.nan_to_num(numeric_features, nan=0.0)

    return np.hstack((tfidf_matrix.toarray(), numeric_features))


# Function to recommend products based on sustainability score and ML-based selections
def recommend_ml_based(products, user_selected_products):
    all_products = user_selected_products + products
    product_vectors = vectorize_products(all_products)

    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(product_vectors)

    # Get the similarities of the last added (user's selection) with all others
    user_similarities = similarity_matrix[0, 1:]

    # Sort by similarity score
    recommendations = np.argsort(-user_similarities)

    # Return the top recommended products (excluding user's own selections)
    return [products[i] for i in recommendations[:5]]


# Function to recommend similar products based on sustainability score
def recommend_similar_products(products, current_product, price_range=15):
    current_score = current_product['sustainability_score']
    current_price = parse_price(current_product['price'])
    current_keywords = extract_keywords(current_product['description'])

    recommendations = []

    for product in products:
        product_score = product['sustainability_score']
        product_price = parse_price(product['price'])
        product_keywords = extract_keywords(product['description'])

        # Check if product meets criteria (similar price range, higher sustainability score, keyword overlap)
        if product_score >= current_score and abs(product_price - current_price) <= price_range:
            keyword_match_count = len(current_keywords.intersection(product_keywords))
            recommendations.append((product, keyword_match_count))

    # Sort recommendations by keyword matches and return top 5
    recommendations.sort(key=lambda x: (-x[1], x[0]['price']))  # prioritize by keyword matches and price
    return [r[0] for r in recommendations[:5]]


# Example usage
def main():
    # Fetch products from MongoDB
    products = list(products_collection.find())

    # User selected products
    user_selected_products = [
        products[0]  # Assuming the first product is selected by the user
    ]

    # Get recommendations based on sustainability score and ML-based past selections
    recommended_products = recommend_ml_based(products, user_selected_products)
    print("ML-based Recommendations:", recommended_products)

    similar_recommended_products = recommend_similar_products(products, user_selected_products[0])
    print("Sustainability Recommendations:", similar_recommended_products)


# Run the main function
if __name__ == "__main__":
    main()
