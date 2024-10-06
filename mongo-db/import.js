
const { MongoClient, ServerApiVersion } = require('mongodb');
const fs = require('fs');
require('dotenv').config(); 

const url = process.env.MONGODB_URI; 
const dbName = process.env.DB_NAME; 

const fileStream = fs.createReadStream('data.jsonl');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  crlfDelay: Infinity
});

const client = new MongoClient(url, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

client.connect();

(async () => {
  try {
    const db = client.db(dbName);
    
    rl.on('line', async (line) => {
      try {
        const item = JSON.parse(line); 
        const collectionName = item.type;
        console.log(collectionName)
        const collection = db.collection(collectionName);

        await collection.insertOne(item);
        console.log(`inserted into ${collectionName}:`, item);
      } catch (error) {
        console.error('error parsing JSON:', error);
      }
    });
    
  } catch (error) {
    console.error('error connecting to MongoDB:', error);
  } finally {
    await client.close();
  }
})();
