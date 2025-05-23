from pprint import pprint
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

uri = "mongodb://localhost:27017"

# Create a new client and connect to the server
client = MongoClient(uri)

def create_database():
    pets_db = client.pets_db
    pets_db.drop_collection("kind_collection")
    kind_collection = pets_db.kind_collection
    kind_collection.insert_many(
        [
            {"kind_name": "Dog", "food": "Dog food", "noise": "Bark"},
            {"kind_name": "Cat", "food": "Cat food", "noise": "Meow"},
            {"kind_name": "Fish", "food": "Fish flakes", "noise": "Blub"},
        ]
    )
    kinds = list(kind_collection.find())
    pprint(kinds)
    pets_db.drop_collection("pets_collection")
    pets_collection = pets_db.pets_collection
    pets = [
        {"name": "Suzy", "age": 3, "kind_name": "Dog", "owner": "Greg"},
        {"name": "Sandy", "age": 2, "kind_name": "Cat", "owner": "Steve"},
        {"name": "Dorothy", "age": 1, "kind_name": "Dog", "owner": "Elizabeth"},
        {"name": "Heidi", "age": 4, "kind_name": "Dog", "owner": "David"},
    ]
    for pet in pets:
        for kind in kinds:
            if kind["kind_name"] == pet["kind_name"]:
                pet["kind_id"] = kind["_id"]
        del pet["kind_name"]
        assert "kind_id" in pet.keys()
    pets_collection.insert_many(pets)
    pets = list(pets_collection.find())
    pprint(pets)

if __name__ == "__main__":
    create_database()
    print("done.")
