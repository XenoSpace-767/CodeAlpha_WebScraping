# CodeAlpha_WebScraping

A Python web scraper that extracts book data from [books.toscrape.com](http://books.toscrape.com) — a sandbox site designed for scraping practice.

## 📌 Project Overview

This project was built as part of the **CodeAlpha Data Analytics Internship**. It demonstrates how to:

- Send HTTP requests and handle responses
- Parse HTML using BeautifulSoup
- Extract structured data from web pages
- Handle pagination across multiple pages
- Clean and save data to CSV using pandas

## 📊 Dataset

- **Source:** http://books.toscrape.com
- **Records:** 1000 books
- **Fields:**
  | Column | Type | Description |
  |--------|------|-------------|
  | `title` | string | Book title |
  | `price` | float | Price in GBP (£) |
  | `rating` | integer | Star rating (1–5) |
  | `availability` | string | Stock status |

## 🛠️ Tech Stack

- Python 3
- `requests` — HTTP requests
- `beautifulsoup4` — HTML parsing
- `pandas` — data cleaning & CSV export

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/CodeAlpha_WebScraping.git
cd CodeAlpha_WebScraping

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scraper
python scraper.py
