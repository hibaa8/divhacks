import re
import pymongo

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

# Function to extract fabric type from product details
def extract_fabric_type(product_details):
    match = re.findall(r'(\d+)%\s*(\w+)', product_details.lower())
    fabric_dict = {}
    if match:
        for percentage, fabric in match:
            fabric_dict[fabric] = int(percentage)
    return fabric_dict

# Function to compute sustainability score based on fabric types
def compute_sustainability_score(fabric_dict):
    score = 0
    total_percentage = 0
    for fabric, percentage in fabric_dict.items():
        if fabric in sustainability_data:
            score += sustainability_data[fabric] * (percentage / 100)
            total_percentage += percentage
    return score if total_percentage > 0 else 0

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]  # replace with your database name
products_collection = db["products"]  # replace with your collection name

# Process each product and calculate sustainability scores
def update_sustainability_scores():
    for product in products_collection.find():
        fabric_dict = extract_fabric_type(product['product_details'])
        score = compute_sustainability_score(fabric_dict)

        # Update the product with the calculated sustainability score
        products_collection.update_one(
            {'_id': product['_id']},
            {'$set': {'sustainability_score': score}}
        )
        print(f"Updated product ID {product['_id']} with sustainability score: {score}")

# Run the update function
update_sustainability_scores()
