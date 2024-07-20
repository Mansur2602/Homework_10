import requests
from bs4 import BeautifulSoup

url = "https://pogoda.mail.ru/prognoz/astana/24hours/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

temperature = soup.find(class_="p-forecast__temperature-value")
print(f"Температура в Астане: {temperature.text}")
