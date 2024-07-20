import aiohttp
import asyncio
import os
from bs4 import BeautifulSoup

os.makedirs("images_books_aiohttp", exist_ok=True)

async def main():
    async with aiohttp.ClientSession() as session:
        page_url = "https://books.toscrape.com/catalogue/page-1.html"
        async with session.get(page_url) as response:
            html = await response.text()

        bs4 = BeautifulSoup(html, "html.parser")
        image_urls = ["https://books.toscrape.com/" + img['src'] for img in bs4.find_all("img")]

        for i, url in enumerate(image_urls[:10]):  
            async with session.get(url) as response:
                image_content = await response.read()
                filename = f"images_books_aiohttp/image_{i+1}.jpg"
                with open(filename, "wb") as f:
                    f.write(image_content)


asyncio.run(main())

