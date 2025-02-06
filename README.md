# web-scrapping

This repository contains multiple web scraping projects using Python. The projects are organized into subfolders, each focused on different scraping techniques and targets. Below is a breakdown of each subfolder and its contents:

## Subfolders

### 1. `gitpro`
This folder contains Python programs used for scraping data from GitHub. The scripts scrape data related to specific topics on GitHub, and the collected data is saved in CSV format. These programs help gather and organize repository-related information for further analysis.

- **Scraping GitHub Data**: The Python scripts in this folder are designed to extract data such as repositories, topics, stars, and other relevant information from GitHub.
- **Scraped Data**: The data scraped by these scripts is saved in `.csv` format for easier processing and analysis.

#### Files:
- `scrape_github_data.py`: Main script to scrape data from GitHub.
- `github_data.csv`: Example of the scraped data in CSV format.

### 2. `project2`
This folder contains a Python program for scraping movie-related data from the MoviesDB website. The program collects movie details such as titles, genres, ratings, and more.

- **Scraping Movies Data**: This script is designed to scrape various details about movies from the MoviesDB site.

#### Files:
- `scrape_movies_data.py`: Python script to scrape movie data.
- `movies_data.csv`: Example of the scraped movie data saved in CSV format.

### 3. `project3`
This folder contains a Python program for scraping dynamic websites using Selenium and BeautifulSoup. These tools are used to handle websites that rely on JavaScript to load content dynamically.

- **Scraping Dynamic Websites**: This project demonstrates how to handle and scrape content from websites that load data dynamically (e.g., through JavaScript rendering).
- **Technologies Used**: The program uses Selenium for rendering JavaScript-heavy content and BeautifulSoup for parsing the HTML.

#### Files:
- `scrape_dynamic_website.py`: Python script to scrape data from a dynamic website using Selenium and BeautifulSoup.
- `dynamic_website_data.csv`: Example of scraped data from a dynamic website saved in CSV format.

## Requirements

- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `selenium`
  - `csv`
  
  You can install the required libraries using `pip`:
  ```bash
  pip install requests beautifulsoup4 pandas selenium

