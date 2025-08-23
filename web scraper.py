import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/page/1/'

# Make a GET request
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all quote blocks
quotes = soup.find_all('div', class_='quote')

# Extract and print quotes and authors
for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    print(f"Quote: {text}\nAuthor: {author}\n")