import json
# mock db
def load_data():
    with open("flashcards_db.json") as f:
        return json.load(f)

db = load_data()