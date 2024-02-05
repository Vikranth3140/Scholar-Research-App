from flask import Flask, render_template, request
from serpapi import GoogleSearch

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        scholar_name = request.form["scholar_name"]
        profile_info = get_scholar_profile(scholar_name)
        return render_template("index.html", profile_info=profile_info)

    return render_template("index.html")

def get_scholar_profile(scholar_name):
    # Serpapi code to get scholar profile information
    api_key = "YOUR_SERPAPI_API_KEY"
    params = {
        "engine": "google_scholar_profiles",
        "mauthors": scholar_name,
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    
    # Extract relevant information from the results
    profile_info = results.get("profiles", [])

    return profile_info

if __name__ == "__main__":
    app.run(debug=True)