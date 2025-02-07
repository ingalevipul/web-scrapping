# web-scrapping

This repository contains multiple web scraping projects implemented in Python. The projects are organized into subfolders, each focusing on different scraping techniques and targets. Below is a detailed breakdown of each subfolder and its contents:

## Project Structure

### 1. `Git_ProE2S`
This folder contains Python scripts used to scrape data from GitHub. The scripts collect information about repositories, topics, stars, and other relevant details related to various topics like JavaScript, Java, and Python. The scraped data is saved in CSV format for easy analysis.

- **Scraping GitHub Data**: The Python scripts in this folder are designed to extract repository-related information, including topics, stars, and more from GitHub.
- **Scraped Data**: The data is saved in `.csv` format for easy processing and analysis.

#### Files:
- `topic_Scrap.py`: Main script to scrape data related to topics from GitHub.
- `topic_data.csv`: Example of scraped data, saved in CSV format.

---

### 2. `Project_no_2`
This folder contains a Python script designed to scrape movie-related data from [The Movie Database (TMDb)](https://www.themoviedb.org). The program collects various movie details, such as titles, genres, ratings, and more.

- **Scraping Movie Data**: This script fetches detailed information about movies, including metadata like genres, titles, ratings, etc., from the TMDb site.

#### Files:
- `main.py`: Python script to scrape movie data from TMDb.
- `Movie_Data.csv`: Example of the scraped movie data saved in CSV format.

---

### 3. `Project_no_3`
This folder contains a Python program that scrapes data from [Trustpilot](https://www.trustpilot.com) using Selenium and BeautifulSoup. The program gathers data from various categories such as "Restaurants & Bars," "Health & Medical," "Hobbies & Crafts," "Financial Institutions," and more.

- **Scraping Dynamic Websites**: This project demonstrates how to handle dynamic websites that load content via JavaScript (e.g., Trustpilot).
- **Technologies Used**: The project relies on **Selenium** for interacting with the dynamic content and **BeautifulSoup4** for parsing the HTML data.

#### Files:
- `Category.py`: Python script to scrape data from specific categories on Trustpilot.
- `Category_DATA.csv`: Example of the scraped data, saved in CSV format.

---

## Requirements

Ensure you have Python 3.8 or higher installed. You will also need the following Python libraries:

- `requests`
- `beautifulsoup4`
- `pandas`
- `selenium`

You can install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4 pandas selenium
