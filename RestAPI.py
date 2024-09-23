import csv
from flask import Flask, jsonify

app = Flask(__name__)

def read_csv():
    characters = []
    with open('characters.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            characters.append({
                "name": row["name"],
                "location": row["location"],
                "image": row["image"]
            })
    return characters

@app.route('/characters', methods=['GET'])
def get_characters():
    characters = read_csv()
    return jsonify(characters)  

@app.route('/healthcheck', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)