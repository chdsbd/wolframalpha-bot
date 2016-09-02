import os

import wolframalpha
from flask import Flask, redirect, request, jsonify

API_KEY = os.getenv('API_KEY')
TOKEN = os.getenv('TOKEN')

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if API_KEY is None or TOKEN is None:
        return 'Missing configuration for API_KEY and/or TOKEN', 500
    if request.method == 'GET':
        return 'Looking good!'
    if request.form['token'] != TOKEN:
        return 'Unauthorized', 401
    query = request.form['text']
    client = wolframalpha.Client(API_KEY)
    res = client.query(query)
    return jsonify({'text': next(res.results).text})
    
if __name__ == "__main__":
    app.run(debug=True)