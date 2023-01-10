
# Amazon Jobs Scraper

This repository contains a script that scrapes the jobs from Amazon's career page. The script uses the `requests` library to send GET requests to the Amazon job search API and the `json` library to convert the data to a JSON format and saves the data in a file named `jobs.json`.

## Requirements

This script is written in Python 3 and requires the following libraries to be installed:

-   requests
-   json

## Usage

1.  Clone or download this repository to your local machine
2.  Open a command line interface and navigate to the directory where you saved the script
3.  Install the required libraries by running `pip install -r requirements.txt`
4.  Run the script by typing `python amazon_jobs_scraper.py`
5.  The script will create a `jobs.json` file in the same directory containing the scraped job data.

## Customization

You can customize the script by modifying the headers, params and the query string in the script to get the jobs according to your preference and location.

## Note

Please note that scraping web pages, especially scraping web pages that don't allow it, is a sensitive subject. Always check the website's terms of service before scraping, and be considerate of their resources and load. Also, you will not be able to execute this code as-is because you need permission and credentials to access Amazon job application.

This script is for educational and learning purposes only. The developer of the script is not responsible for any damage caused by the misuse of this script.