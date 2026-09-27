import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []

for page in range(1, 51):

    url = base_url.format(page)

    print(f"Scraping page {page}...")

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to access page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.select_one(".price_color").text.strip()

        rating = book.select_one("p.star-rating")["class"][1]

        availability = book.select_one(".availability").text.strip()

        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

df = pd.DataFrame(data)

df.to_excel("books_data.xlsx", index=False)

print("\n--------------------------------")
print("DATA EXTRACTION COMPLETED")
print("--------------------------------")
print(f"Total books extracted: {len(df)}")
print("Excel file created: books_data.xlsx")