import requests
import os
from bs4 import BeautifulSoup


os.makedirs("images_books_requests", exist_ok=True)


page_url = "https://books.toscrape.com/catalogue/page-1.html"

response = requests.get(page_url)
html = response.text
bs4 = BeautifulSoup(html, "html.parser")


image_urls = ["https://books.toscrape.com/" + img['src'] for img in bs4.find_all("img")]

for i, url in enumerate(image_urls[:10]): 
    response = requests.get(url)
    filename = f"images_books_requests/image_{i+1}.jpg"
    with open(filename, "wb") as f:
        f.write(response.content)
