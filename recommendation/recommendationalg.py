import re

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
    'description': "Women's Ruffle Funny Ankle Socks,Cute Smiling Face Embroidery Frilly Crew Sock...",
    'brand': 'Brand: XIUYANG',
    'color': 'Color: Colour-a'
}


# 1. Extract fabric type from product details
def extract_fabric_type(product_details):
    # Find fabric type percentages (e.g., "80% cotton")
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
    return score if total_percentage > 0 else None


# 3. Parse the price into a float
def parse_price(price_str):
    price_str = price_str.replace('\n', '').replace('$', '').strip()
    try:
        return float(price_str)
    except ValueError:
        return None


# 4. Extract keywords from description for similarity matching
def extract_keywords(description):
    # Tokenize and lower case the description
    keywords = re.findall(r'\b\w+\b', description.lower())
    return set(keywords)


# 5. Final recommendation function based on price range, sustainability score, and keywords
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
    # Add other product dictionaries with similar structure here for recommendation comparison
]

recommended_products = recommend_similar_products(products, product_data)
print(recommended_products)
