import os
import json
from pymongo import MongoClient


from dotenv import load_dotenv
load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')  
DB_NAME = os.getenv('DB_NAME')  

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

jsonl_file = 'more-tops.jsonl'

def insert_data():
    try:
        with open(jsonl_file, 'r') as file:
            for line in file:
                try:
                    item = json.loads(line)
                    
                    collection_name = item['type'].lower()  
                    collection = db[collection_name]
                    
                    collection.insert_one(item)
                    print(f"Inserted into {collection_name}: {item}")

                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                except Exception as e:
                    print(f"Error inserting into MongoDB: {e}")
    except Exception as e:
        print(f"Error reading file: {e}")
    finally:
        client.close()

# Run the insertion process
if __name__ == "__main__":
    insert_data()
