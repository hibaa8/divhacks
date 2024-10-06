import random
import json


brands = ["Pact", "Everlane", "Quince", "People Tree", "Thought Clothing"]


fabrics = {
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

types = ["shirt", "pant", "sweater", "jacket"]

def generate_clothing_item(clothing_type):
    fabric = random.choice(list(fabrics.keys()))  
    percentage = random.randint(50, 100)  
    brand = random.choice(brands)  
    price = random.randint(40, 150)  

    return {
        "fabric": f"{percentage}% {fabric.capitalize()}",
        "price": str(price), 
        "description": f"A sustainable {clothing_type} made from {percentage}% {fabric}.",
        "brand": brand,
        "color": random.choice(["Black", "Blue", "Green", "Red", "Purple", "Beige", "Pink", "Orange"]),
        "type": clothing_type, 
        "url": "url",
        "image": "image"
    }

all_clothing_items = []

for clothing_type in types:
    for _ in range(20):
        item = generate_clothing_item(clothing_type)
        all_clothing_items.append(item)

with open('generated_data.jsonl', 'w') as f:
    for item in all_clothing_items:
        f.write(json.dumps(item) + '\n')

for item in all_clothing_items[:5]:  
    print(json.dumps(item, indent=4))
