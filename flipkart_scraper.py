import logging
from concurrent.futures import ThreadPoolExecutor
import requests
import pandas as pd
import time
import random
from bs4 import BeautifulSoup

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Headers for requests
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.flipkart.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}

# Function to fetch a single page
def fetch_page(page):
    """Fetches the HTML content of a Flipkart search results page."""
    url = f"https://www.flipkart.com/search?q=5g+smartphone&page={page}"
    session = requests.Session()  # Create a new session for each request
    session.headers.update(HEADERS)

    try:
        time.sleep(random.uniform(2, 4))  # Random delay to avoid blocking
        response = session.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching page {page}: {e}")
        return None

# Function to parse a single page
def parse_page(html):
    """Parses product data from a Flipkart search results page."""
    soup = BeautifulSoup(html, "lxml")

    # Extract product details
    names = soup.find_all("div", class_="KzDlHZ")  # Product Name
    prices = soup.find_all("div", class_="Nx9bqj _4b5DiR")  # Price
    descriptions = soup.find_all("ul", class_="G4BRas")  # Description
    ratings = soup.find_all("div", class_="XQDdHH")  # Ratings

    data = []
    for name, price, desc, rating in zip(names, prices, descriptions, ratings):
        data.append({
            "Product Name": name.text.strip(),
            "Price": price.text.replace("₹", "").replace(",", "").strip(),
            "Description": desc.text.strip(),
            "Rating": rating.text.strip() if rating else "No rating"
        })

    return data

# Main scraping function
def scrape_flipkart():
    """Scrapes multiple Flipkart pages and saves data to CSV."""
    all_data = []
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_page, page) for page in range(1, 31)]
        
        for future in futures:
            html = future.result()
            if html:
                all_data.extend(parse_page(html))

    # Create DataFrame and save to CSV
    df = pd.DataFrame(all_data)
    df.to_csv("Flipkart_Data.csv", index=False)
    logging.info("Scraping completed and data saved to Flipkart_Data.csv")

if __name__ == "__main__":
    scrape_flipkart()
