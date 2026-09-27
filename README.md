# 📚 Books Data Extraction & Web Scraping

This project demonstrates **web scraping** of 1,000 books from [books.toscrape.com](https://books.toscrape.com), followed by **data cleaning** and analysis in Excel.

**Author:** Bramwel Mwasenga
🔗 Portfolio: https://bramwelsamwel16.github.io/portifolio/
🔗 GitHub: https://github.com/bramwelsamwel16

---

## 🎯 Project Goal

To demonstrate the ability to:
- Extract data directly from a website (web scraping) using Python
- Clean messy, unstructured data using Excel
- Analyze and summarize data using Excel formulas

---

## 🛠️ Tools & Technologies Used

| Task | Tool |
|---|---|
| Web scraping | **Python** (`requests`, `BeautifulSoup4`) |
| Data storage | **Pandas** (`to_excel`) |
| Writing & testing code | **Visual Studio Code (VS Code)** |
| Data cleaning & analysis | **Microsoft Excel** (openpyxl-generated workbook, tables, formulas, formatting) |
| Version control | **Git & GitHub** |
| Portfolio hosting | **GitHub Pages** |

---

## 📂 Project Structure

```
books-data-extraction/
│
├── scraper.py                          # Python web scraping script
├── books_data.xlsx                     # Raw data straight from the scraper
├── books_data_CLEANED.xlsx             # Cleaned data + statistical summary
├── Books_Data_Extraction_Portfolio.pdf # Full portfolio report (screenshots + explanations)
└── README.md                           # This file
```

---

## 🔄 How the Data Was Extracted

1. `scraper.py` visits 50 catalogue pages at `books.toscrape.com/catalogue/page-{n}.html`
2. For each page, `requests.get()` downloads the page's HTML
3. `BeautifulSoup` locates every book (`article.product_pod`) and extracts:
   - **Title** – the book's name
   - **Price** – price (in £)
   - **Rating** – star rating (star-rating class, e.g. "Three")
   - **Availability** – stock status
4. All records are collected into a list of dictionaries and converted into a **Pandas DataFrame**
5. The DataFrame is saved as `books_data.xlsx` using `df.to_excel()`

Result: **1,000 books** from 50 pages (20 books per page).

### How to run the scraper

```bash
pip install requests beautifulsoup4 pandas openpyxl
python scraper.py
```

---

## 🧹 Data Cleaning Summary

The raw data had the following issues, all resolved in `books_data_CLEANED.xlsx`:

1. **Price** was stored as text with a `£` symbol (e.g. `£51.77`) — converted into a numeric column `Price (GBP)` so it can be used in calculations.
2. **Rating** was stored as words (`One`–`Five`) instead of numbers — a numeric column `Rating (1-5)` was added.
3. **Availability** has only one value (`In stock`) for all 1,000 books — this column has limited analytical value.
4. **Duplicate record**: the book *"The Star-Touched Queen"* appears twice at different prices — kept and flagged transparently.
5. No missing values were found.

Full details of the issues and how they were resolved are in the **"Maelezo ya Usafishaji" (Cleaning Notes)** sheet inside `books_data_CLEANED.xlsx`, and in the portfolio PDF.

---

## 📊 Key Insights

- Average price across all 1,000 books: **£35.07**
- Highest price: **£59.99** | Lowest price: **£10.00**
- Average rating: **2.92 / 5**
- Rating distribution: 1★ = 226 books, 2★ = 196, 3★ = 203, 4★ = 179, 5★ = 196
- All books (100%) are listed as "In stock"

---

## 📎 Key Files

- [`scraper.py`](./scraper.py) — Python scraping script
- [`books_data.xlsx`](./books_data.xlsx) — raw data
- [`books_data_CLEANED.xlsx`](./books_data_CLEANED.xlsx) — cleaned data + summary
- [`Books_Data_Extraction_Portfolio.pdf`](./Books_Data_Extraction_Portfolio.pdf) — full report with screenshots

---

## 👤 Author

**Bramwel Mwasenga**
- Portfolio: [bramwelsamwel16.github.io/portifolio](https://bramwelsamwel16.github.io/portifolio/)
- GitHub: [@bramwelsamwel16](https://github.com/bramwelsamwel16)
