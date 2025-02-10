# Flipkart-Mobile-Scraper

This Python script scrapes details of any product from Flipkart, including product names, prices, descriptions, and ratings. The scraped data is saved into a CSV file.

## Features
- Extracts product details such as:
  - Product Name
  - Price
  - Description
  - Rating
- Scrapes multiple pages (up to 50)
- Saves data in a structured CSV file

## Requirements
Make sure you have the following Python libraries installed before running the script:

```sh
pip install requests beautifulsoup4 lxml pandas numpy
```

## Usage
Run the script using Python:

```sh
python scraper.py
```

### Output
- The script will generate a `Flipkart_Data.csv` file containing the scraped data.

## How It Works
1. Sends requests to Flipkart’s search page for product.
2. Parses the webpage using BeautifulSoup.
3. Extracts the required details using HTML classes.
4. Saves the extracted data into a CSV file.

## Notes
- Flipkart may update their HTML structure, requiring adjustments to the scraping logic.
- Excessive scraping may lead to IP blocking; use delays or proxies if necessary.

## Disclaimer
This project is for educational purposes only. Scraping e-commerce websites may violate their terms of service. Use responsibly.
