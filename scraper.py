import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# Empty list to store all books
book_data = []

# Looping through 50 pages
for page in range(1, 51):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"Scraping Page {page}...")

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve Page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text.strip()

        rating = book.find("p", class_="star-rating")["class"][1]

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        # Get the book URL
        relative_url = book.h3.a["href"]
        book_url = urljoin(url, relative_url)

        # Storing data
        book_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Book URL": book_url
        })

# Creating DataFrame
df = pd.DataFrame(book_data)

# Save to CSV
df.to_csv("books1.csv", index=False)

print("\nScraping Complete!")
print(f"Total books collected: {len(df)}")

print("\nFirst five books:")
print(df.head())
