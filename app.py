from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://root:admin@localhost:27017/')
db = client['recipe-database']
collection = db['recipes']

@app.route('/register', methods=['POST'])
def create_recipe():
    print("oi")
    name = request.form['name']
    description = request.form['description']
    ingredients = request.form.getlist('ingredients')
    print(name)
    print(description)
    for ingredient in ingredients:
        print(ingredient)
    return jsonify({"message": "Success"})

@app.route('/register', methods=['GET'])
def recipe():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)