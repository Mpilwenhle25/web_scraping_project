# Books to Scrape - Web Scraping Project

## Project Overview

This project demonstrates basic web scraping techniques using Python. It collects book information from the Books to Scrape website and stores the data in a CSV file.

## Website

https://books.toscrape.com/

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas

## Data Collected

- Book Title
- Price
- Rating
- Availability
- Book URL

## Features

- Downloads webpages using HTTP requests.
- Parses HTML using BeautifulSoup.
- Extracts book information.
- Handles pagination across all 50 pages.
- Stores the collected data in CSV format.

## Output

The scraper collects approximately **1000 books** and saves them as:

```
books_raw.csv
```

## How to Run

Install the required libraries:

```bash
pip install requests beautifulsoup4 pandas
```

Run the scraper:

```bash
python scraper.py
```
