import requests
import numpy as np
import pandas as pd
import time
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.flipkart.com/",  # Replace with the actual site if needed
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}

Product_name = []
Price = []
Description = []
Rating = []

for i in range(1,51):
    url = "https://www.flipkart.com/search?q=5g+smartphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&as-pos=1&as-type=RECENT&suggestionId=5g+smartphone%7CMobiles&requestId=389d16cf-dff9-45b9-8517-98d6471063f6&as-searchtext=5g+smartphone&page=" + str(i)

    webpage = requests.get(url, headers = headers)

    soup = BeautifulSoup(webpage.text, "lxml")

    # Fetch Mobile names from webpage
    names = soup.find_all("div", class_ = "KzDlHZ")

    for i in names:
        name = i.text
        Product_name.append(name)

    # Fetch Mobile Prices from webpage
    prices = soup.find_all("div", class_ = "Nx9bqj _4b5DiR")

    for i in prices:
        price = i.text
        Price.append(price)

    # Fetch Mobile Description from webpage
    desc = soup.find_all("ul", class_ = "G4BRas")

    for i in desc:
        description = i.text
        Description.append(description)

    # Fetch Mobile Rating from webpage
    box = soup.find("div", class_ = "DOjaWF gdgoEp")
    rating = box.find_all("div", class_ = "XQDdHH")

    for i in rating:
        rating = i.text
        Rating.append(rating)

df = pd.DataFrame({"Product Name" : Product_name, "Price" : Price, "Description" : Description, "Rating" : Rating})

print(df)

df.to_csv("Flipkart_Data.csv")
