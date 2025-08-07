"""
1. Create a Flask application with an /api route. 
   When this route is accessed, it should return a JSON list. 
   The data should be stored in a backend file, read from it, and sent as a response.
2. Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas. 
   Upon successful submission, the user should be redirected to another page 
   displaying the message "Data submitted successfully". 
   If there's an error during submission, display the error on the same page 
   without redirection
"""

from flask import Flask,jsonify,request
import json
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
import os

uri = os.getenv("uri")
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test  #creates database named test
collection = db['flask-assessment']  #creates collection named flask-assessment

app = Flask(__name__)
@app.route('/view')
def get_data():
    with open("data.json","r") as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/submit', methods=['POST'])
def submit_data():
    form_data = request.json
    collection.insert_one(form_data)
    return 'Data submitted successfully'

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 7000,debug=True)
