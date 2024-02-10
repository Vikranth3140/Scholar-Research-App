# Scholar Research App

The Scholar Research App is a web application that allows users to fetch and display Google Scholar papers for a given scholar's name. The app utilizes the <a href="https://serpapi.com/">SerpApi</a> to retrieve search results from <a href="https://scholar.google.com/">Google Scholar</a>.


## Features

- Enter the scholar's name and get their research papers list.
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


## Tech Stack

- HTML, CSS
- Flask (Python)
- SerpApi


## How to Use

1. **Installation:**
   - Clone the repository.

    ```bash
    git clone https://github.com/Vikranth3140/Scholar-Research-App.git
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

4. **View Results:**
   - Open the app in your web browser.

        [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

   - The application will display real-time research paper information and the corresponding paper links.

## Note

- Keep your API keys confidential and do not share them publicly.
- Ensure an active internet connection for accurate data retrieval.


## Future Enhancements

If you're looking for ideas on how to enhance this project, consider the following improvements:

1. **Google Scholar Integration:**
   - Explore the possibility of integrating with the Google Scholar API for more accurate and detailed profile information.

2. **Improved UI/UX:**
   - Enhance the user interface for a more intuitive and user-friendly experience.
   - Add features like loading spinners or notifications to improve user feedback.

3. **Additional Scholar Metrics:**
   - Expand the application to fetch and display additional scholar metrics and statistics.

4. **Localization:**
   - Implement multi-language support for a broader user base.

5. **Optimization:**
   - Optimize API calls and application performance.

6. **Bug Fixes:**
   - Address any reported bugs and issues.

7. **Documentation:**
   - Improve and expand project documentation for better understanding and onboarding of contributors.


## Contributing

Welcome to contribute to Scholar H-Index App! Feel free to fork the repository and suggest any improvements. To contribute, follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push the changes to your fork.
5.  Submit a pull request.

Thank you for your contributions!


## License

This project is licensed under the [MIT License](LICENSE).


## Author

[Vikranth Udandarao](https://github.com/Vikranth3140)