import requests
from config import SERPAPI_KEY

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

def main():
    query = "biology"  # Change the query as needed
    total_chunks = 3  # Set the total number of chunks
    current_chunk = 1

    while current_chunk <= total_chunks:
        start_index = (current_chunk - 1) * 10
        results = fetch_serpapi_results(query, start=start_index)

        # Process and use the results as needed
        print(f"Processing results for chunk {current_chunk}/{total_chunks}")
        print(results)

        current_chunk += 1

if __name__ == "__main__":
    main()