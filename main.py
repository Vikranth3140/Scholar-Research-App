from flask import Flask, render_template, request
import requests
from config import SERPAPI_KEY

app = Flask(__name__)

def fetch_serpapi_results(query, start=0):
    api_key = SERPAPI_KEY
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

def calculate_h_index(papers):
    citations = [paper.get("cited_by_count", 0) for paper in papers]
    citations.sort(reverse=True)
    h_index = 0

    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break

    return h_index

@app.route('/', methods=['GET', 'POST'])
def index():
    paper_details = []
    h_index = 0

    if request.method == 'POST':
        query = request.form['scholarName']
        total_chunks = 3
        current_chunk = 1

        while current_chunk <= total_chunks:
            start_index = (current_chunk - 1) * 10
            api_results = fetch_serpapi_results(query, start=start_index)
            paper_details.extend(api_results["organic_results"])
            current_chunk += 1

        h_index = calculate_h_index(paper_details)

    return render_template('index.html', paper_details=paper_details, h_index=h_index)

if __name__ == "__main__":
    app.run(debug=True)