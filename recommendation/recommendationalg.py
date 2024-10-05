import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Updated sustainability data
sustainability_data = {
    "organic cotton": 10,
    "hemp": 9,
    "bamboo": 8,
    "recycled polyester": 7,
    "linen": 8,
    "tencel (lyocell)": 8,
    "recycled wool": 7,
    "conventional cotton": 5,
    "silk": 5,
    "recycled nylon": 6,
    "polyester": 3,
    "nylon": 2,
    "acrylic": 3,
    "spandex": 4,
    "viscose": 5,
    "leather (sustainable)": 6,
    "leather (conventional)": 3,
    "PVC (faux leather)": 2,
    "cupro": 7,
    "jute": 9,
    "ramie": 8,
    "modal": 7,
    "wool": 6,
    "alpaca wool": 7,
    "recycled acrylic": 5
}

# Example input product details
product_data = {
    'product_details': 'Fabric type\n80% cotton\nCare instructions\nMachine Wash\n...',
    'price': '$13\n89',
    'description': "Women's Ruffle Funny Ankle Socks...",
    'brand': 'Brand: XIUYANG',
    'color': 'Color: Colour-a'
}

# 1. Extract fabric type from product details
def extract_fabric_type(product_details):
    match = re.findall(r'(\d+)%\s*(\w+)', product_details.lower())
    fabric_dict = {}
    if match:
        for percentage, fabric in match:
            fabric_dict[fabric] = int(percentage)
    return fabric_dict

# 2. Compute sustainability score based on fabric types
def compute_sustainability_score(fabric_dict):
    score = 0
    total_percentage = 0
    for fabric, percentage in fabric_dict.items():
        if fabric in sustainability_data:
            score += sustainability_data[fabric] * (percentage / 100)
            total_percentage += percentage
    return score if total_percentage > 0 else 0  # Return 0 if no valid fabric types

# 3. Parse the price into a float
def parse_price(price_str):
    price_str = price_str.replace('\n', '').replace('$', '').strip()
    try:
        return float(price_str)
    except ValueError:
        return 0.0  # Return 0 if parsing fails

# 4. Extract keywords from description for similarity matching
def extract_keywords(description):
    keywords = re.findall(r'\b\w+\b', description.lower())
    return set(keywords)

# 5. Vectorize products for content-based filtering using description and sustainability score
def vectorize_products(products):
    vectorizer = TfidfVectorizer()

    descriptions = [' '.join(extract_keywords(product['description'])) for product in products]
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    numeric_features = np.array([[parse_price(product['price']),
                                  compute_sustainability_score(extract_fabric_type(product['product_details']))]
                                 for product in products])

    # Replace NaN values with 0
    numeric_features = np.nan_to_num(numeric_features, nan=0.0)

    return np.hstack((tfidf_matrix.toarray(), numeric_features))

# 6. Calculate similarity between user-selected products and all other products
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

# 7. Final recommendation function based on price range, sustainability score, and keywords
def recommend_similar_products(products, current_product, price_range=15):
    current_fabric_dict = extract_fabric_type(current_product['product_details'])
    current_score = compute_sustainability_score(current_fabric_dict)
    current_price = parse_price(current_product['price'])
    current_keywords = extract_keywords(current_product['description'])

    recommendations = []

    for product in products:
        product_fabric_dict = extract_fabric_type(product['product_details'])
        product_score = compute_sustainability_score(product_fabric_dict)
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
products = [
    {
        'product_details': 'Fabric type\n100% recycled polyester\nCare instructions\nMachine Wash\n...',
        'price': '$18\n99',
        'description': "Women's Recycled Polyester T-Shirt...",
        'brand': 'Brand: GreenThreads',
        'color': 'Color: Blue'
    },
    # Add more product dictionaries for recommendation comparison
]

user_selected_products = [
    {
        'product_details': 'Fabric type\n100% cotton\nCare instructions\nMachine Wash\n...',
        'price': '$13\n89',
        'description': "Women's Ruffle Funny Ankle Socks...",
        'brand': 'Brand: XIUYANG',
        'color': 'Color: Colour-a'
    }
]

# Get recommendations based on sustainability score and ML-based past selections
recommended_products = recommend_ml_based(products, user_selected_products)
print("ML-based Recommendations:", recommended_products)

similar_recommended_products = recommend_similar_products(products, user_selected_products[0])
print("Sustainability Recommendations:", similar_recommended_products)
