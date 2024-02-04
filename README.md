# Scholar H-Index App

The Scholar H-Index App is a web application that allows users to fetch and display Google Scholar <a href="https://en.wikipedia.org/wiki/H-index">H-Index</a> information for a given scholar's name. The app utilizes the <a href="https://serpapi.com/">SerpApi</a> to retrieve search results from <a href="https://scholar.google.com/">Google Scholar</a>.


## Features

- Enter the scholar's name and get the H-Index information.
- Results displayed with paper titles from Google Scholar.


## File Structure

    Scholar_H_Index_App
    │
    ├── static
    │   └── styles
    │       └── styles.css
    │
    ├── templates
    │   └── index.html
    │
    ├── config.py
    ├── main.py
    ├── LICENSE
    ├── README.md
    ├── requirements.txt


## How to Use

1. **Installation:**
   - Clone the repository.

    ```bash
    git clone https://github.com/Vikranth3140/H-Index-Finder.git
    ```

   - Install required dependencies

    ```bash
    pip install -r requirements.txt
    ```

2. **API Configuration:**
   - Obtain your API key from [SerpApi](https://serpapi.com/).
   - Replace `SERPAPI_KEY` in `config.py` your actual key.

3. **Run the Application:**
   - Execute the Python app

    ```bash
    python run main.py
    ```

   - Enter the desired scholor's name.

4. **View Insights:**
   - Open the app in your web browser.

        [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

   - The application will display real-time h-index information and the corresponding paper links.


## Requirements

- Python
- Flask
- HTML, CSS
- SerpApi API key


## Note

- Keep your API keys confidential and do not share them publicly.
- Ensure an active internet connection for accurate data retrieval.


## License

This project is licensed under the [MIT License](LICENSE).


## Author

[Vikranth Udandarao](https://github.com/Vikranth3140)