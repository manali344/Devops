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

from flask import Flask,jsonify,render_template,request
import json
import requests


BACKEND_URL = "http://127.0.0.1:7000"

app = Flask(__name__)
@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    form_data = dict(request.form)
    print("Form Data Received:", form_data) 
    try:
        requests.post(BACKEND_URL + '/submit', json=form_data)
        return render_template('submit_success.html', message="Data submitted successfully")
    except requests.exceptions.RequestException as e:
        print("Error during submission:", e)
        



@app.route('/api',methods=['GET'])
def api():
    try:
        response = requests.get(BACKEND_URL + '/view', timeout=5)
        response.raise_for_status()  # Raises error if status != 200
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print("Error connecting to backend:", e)  # Print to terminal
        return jsonify({"error": "Failed to connect to backend", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=9000,debug=True)