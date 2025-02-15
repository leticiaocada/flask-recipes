from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['recipe-database']
collection = db['recipes']

@app.route('/register', methods=['POST'])
def create_recipe():
    name = request.form['name']
    description = request.form['description']
    ingredients = request.form.getlist('ingredients')
    document = {"name": name, "description": description, "ingredients": ingredients}
    result = collection.insert_one(document)
    if result.__acknowledged == True:
        return jsonify({"message": "Successfull insertion"})
    else:
        return jsonify({"message": "Failed insertion"}), 400
    
@app.route('/searchrecipe', methods=['POST'])
def search_recipe():
    return jsonify({"message": "OK"})

@app.route('/searchrecipe', methods=['GET'])
def render_recipes():
    return render_template('recipes.html')

@app.route('/register', methods=['GET'])
def recipe():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)