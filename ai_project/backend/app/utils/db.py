from pymongo import MongoClient
from datetime import datetime

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "image_analysis_db"
COLLECTION_NAME = "image_metadata"

def get_database():
    """
    Connect to local MongoDB and return the database object.
    """
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        print(f"✅ Connected to MongoDB database: {DB_NAME}")
        return db
    except Exception as e:
        print("❌ Failed to connect to MongoDB:", e)
        return None


def insert_metadata(filename: str, size: int, path: str):
    """
    Insert image metadata (filename, size, storage path, timestamp) into MongoDB.
    """
    db = get_database()
    if db is None:
        print("❌ No database connection. Metadata not saved.")
        return

    data = {
        "filename": filename,
        "size": size,
        "path": path,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        db[COLLECTION_NAME].insert_one(data)
        print(f"✅ Metadata for '{filename}' saved to MongoDB.")
    except Exception as e:
        print("❌ Error inserting metadata:", e)


if __name__ == "__main__":
    # Test connection and insert sample metadata
    db = get_database()
    if db is not None:
        insert_metadata("test_image.jpg", 12456, "storage/images/test_image.jpg")
