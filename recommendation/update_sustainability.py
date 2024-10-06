import re
import pymongo
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
import certifi

load_dotenv()

sustainability_data = {
    "organic": 10,
    "hemp": 9,
    "bamboo": 8,
    "polyester": 7,
    "linen": 8,
    "tencel": 8,
    "cotton": 5,
    "silk": 5,
    "nylon": 6,
    "acrylic": 3,
    "spandex": 4,
    "viscose": 5,
    "leather": 3,
    "PVC": 2,
    "cupro": 7,
    "jute": 9,
    "ramie": 8,
    "modal": 7,
    "wool": 6,
    "alpaca": 7,
    "recycled": 5,
}

class SustainabilityCalculator:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URI"), tlsCAFile=certifi.where())
        self.db = self.client[os.getenv("DB_NAME")]

    def extract_fabric_type(self, fabric):
        components = fabric.split()
        fabric_dict = {}

        for i in range(0, len(components) - 1, 2):
            percentage = components[i]
            fabric = components[i + 1]
            fabric_dict[fabric] = percentage

        return fabric_dict

    def compute_sustainability_score(self, fabric_dict):
        score = 0
        total_percentage = 0
        for fabric, percentage in fabric_dict.items():
    
            if isinstance(percentage, str):
                try:
                    percentage = int(percentage[:2])  
                except ValueError:
                    continue
            percentage = int(percentage)
            fabric = fabric.lower()

            if fabric in sustainability_data:
                score += sustainability_data[fabric] * (percentage / 100)
                total_percentage += percentage

        return score if total_percentage > 0 else 0

    def update_sustainability_scores(self):
        collections = self.db.list_collection_names()

        for collection_name in collections:
            collection = self.db[collection_name]
            for product in collection.find():
                if 'fabric' in product:
                    fabric_dict = self.extract_fabric_type(product['fabric'])
                elif 'product_details' in product:
                    fabric_dict = self.extract_fabric_type(product['product_details'])
                else:
                    continue

                score = self.compute_sustainability_score(fabric_dict)


                collection.update_one(
                    {'_id': product['_id']}, 
                    {'$set': {'env-index': score}}  
                )

                print(f"Updated product ID {product['_id']} with sustainability score: {score}")


# Example usage
if __name__ == '__main__':
    uri = os.getenv("MONGODB_URI")
    db_name = os.getenv("DB_NAME")

    sustainability_calculator = SustainabilityCalculator(uri, db_name)
    sustainability_calculator.update_sustainability_scores()
