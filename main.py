from flask import Flask, render_template, request
import requests
from config import SERPAPI_KEY

app = Flask(__name__)

def fetch_serpapi_results(query, start=0):
    api_key = SERPAPI_KEY  # Replace with your actual SerpApi API key
    base_url = "https://serpapi.com/search.json"
    params = {
        "q": query,
        "hl": "en",
        "as_sdt": "0,38",
        "engine": "google_scholar",
        "start": start,
        "api_key": api_key,
    }

    response = requests.get(base_url, params=params)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    h_index = None

    if request.method == 'POST':
        query = request.form['scholarName']
        total_chunks = 3
        current_chunk = 1

        results = []

        while current_chunk <= total_chunks:
            start_index = (current_chunk - 1) * 10
            api_results = fetch_serpapi_results(query, start=start_index)
            results.extend(api_results["organic_results"])
            current_chunk += 1

        h_index = [result['title'] for result in results]

    return render_template('index.html', h_index=h_index)

if __name__ == "__main__":
    app.run(debug=True)