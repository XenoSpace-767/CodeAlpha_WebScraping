"""
CodeAlpha Internship - Task 1: Web Scraping
Scrapes all 1000 books from books.toscrape.com
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# ---------- SETTINGS ----------
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
TOTAL_PAGES = 50
OUTPUT_FILE = "data/books.csv"

# A dictionary that maps the word in the HTML class to a number
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def scrape_page(page_number):
    """Scrape a single page and return a list of book dictionaries."""
    url = BASE_URL.format(page_number)
    print(f"Scraping page {page_number}: {url}")

    # 1. Send HTTP GET request
    response = requests.get(url, timeout=10)
    response.encoding = "utf-8" 

    # 2. Check if the request succeeded (status code 200 = OK)
    if response.status_code != 200:
        print(f"  Failed! Status code: {response.status_code}")
        return []

    # 3. Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # 4. Find all book containers on the page
    books = soup.find_all("article", class_="product_pod")

    page_data = []

    # 5. Loop through each book and extract its details
    for book in books:
        # Title is inside an <h3><a title="..."></a></h3>
        title = book.h3.a["title"]

        # Price is inside a <p class="price_color">
        price = book.find("p", class_="price_color").text

        # Rating is a class like "star-rating Three"
        rating_class = book.find("p", class_="star-rating")["class"]
        rating_word = rating_class[1]           # "Three"
        rating = RATING_MAP.get(rating_word, 0) # 3

        # Availability text (e.g. "In stock")
        availability = book.find("p", class_="instock availability").text.strip()

        # Append as a dictionary (a row)
        page_data.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
        })

    return page_data


def main():
    """Main function: loop through all pages and save to CSV."""
    all_books = []

    # Loop from page 1 to page 50
    for page in range(1, TOTAL_PAGES + 1):
        books_on_page = scrape_page(page)
        all_books.extend(books_on_page)
        time.sleep(1)  # Be polite: wait 1 second between requests

    print(f"\nTotal books scraped: {len(all_books)}")

    # Convert list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(all_books)

    # Remove any non-numeric characters except the dot (handles Â£, £, $, etc.)
    df["price"] = df["price"].str.replace(r"[^\d.]", "", regex=True).astype(float)

    # Save to CSV
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved to {OUTPUT_FILE}")

    # Show first 5 rows
    print("\nPreview of data:")
    print(df.head())


if __name__ == "__main__":
    main()