from flask import Flask, render_template, request, jsonify
import requests
from config import SERPAPI_KEY

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getHIndex', methods=['POST'])
def get_h_index():
    try:
        scholar_name = request.json.get('scholarName')
        api_key = SERPAPI_KEY
        api_url = 'https://serpapi.com/scholar'

        response = requests.get(api_url, params={'q': scholar_name, 'api_key': api_key})
        data = response.json()

        h_index = data.get('hindex', 'N/A')
        return jsonify({'hIndex': h_index})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)