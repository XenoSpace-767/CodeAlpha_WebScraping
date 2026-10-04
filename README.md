# CodeAlpha_WebScraping

A complete data analytics pipeline built during the **CodeAlpha Data Analytics Internship** — from web scraping to exploratory analysis to data visualization.

## 📌 Project Overview

Three linked tasks, one dataset:

| Task | Description | Notebook/Script |
|------|-------------|-----------------|
| **Task 1** | Web Scraping — extract 1000 books from books.toscrape.com | `scraper.py` |
| **Task 2** | Exploratory Data Analysis — ask questions, test hypotheses | `eda.ipynb` |
| **Task 3** | Data Visualization — 5 charts + dashboard | `visualization.ipynb` |

## 📊 Dataset

- **Source:** http://books.toscrape.com (public sandbox site)
- **Records:** 1000 books
- **Fields:**
  | Column | Type | Description |
  |--------|------|-------------|
  | `title` | string | Book title |
  | `price` | float | Price in GBP (£) |
  | `rating` | integer | Star rating (1–5) |
  | `availability` | string | Stock status |

## 🔍 Key Findings

1. **Price distribution** — Fairly uniform from £10 to £60, mean ≈ £35.
2. **Rating vs price** — Correlation ≈ 0.00 (rating is independent of price).
3. **Data quality** — `availability` has zero variance (all "In stock") — dropped.
4. **Rating balance** — Each tier (1–5 stars) holds ~20% of the catalog.
5. **No outliers** — Price boxplot reveals no extreme anomalies.

## 🛠️ Tech Stack

- Python 3
- `requests`, `beautifulsoup4` — web scraping
- `pandas`, `numpy` — data manipulation
- `matplotlib`, `seaborn` — visualization
- Jupyter Notebook — interactive analysis

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/CodeAlpha_WebScraping.git
cd CodeAlpha_WebScraping

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scraper (takes ~60 seconds)
python scraper.py

# 4. Open the notebooks
jupyter notebook eda.ipynb
jupyter notebook visualization.ipynb
