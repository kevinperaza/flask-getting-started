import json


endpoint = "flashcards_db.json"
# mock db
def load_data():
    with open(endpoint) as f:
        return json.load(f)

def save_db():
    with open(endpoint, 'w') as f:
        return json.dump(db, f)


db = load_data()