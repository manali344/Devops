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

from flask import Flask,jsonify
import json

app = Flask(__name__)
@app.route('/view')
def get_data():
    with open("data.json","r") as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 7000,debug=True)