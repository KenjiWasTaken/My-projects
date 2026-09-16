import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

link = "https://books.toscrape.com/"
response = requests.get(link)
soup = BeautifulSoup(response.text, 'html.parser')

books = []

def find_books():
    global soup

    titles = soup.find_all("a", title=True)
    pricetag = soup.find_all("p", class_='price_color')

    for title, price in zip(titles, pricetag):
        book = {"title" : title['title'], "price" : price.text}
        books.append(book)

    for book in books:
        print(f"{book['title']} - {book['price']}")

    next = soup.find("li", class_='next')
    if next == None:
        return False
    next_link = next.find("a", href=True)

    joined_link = urljoin(link, next_link['href'])
    response = requests.get(joined_link)
    soup = BeautifulSoup(response.text, 'html.parser')

    return True

while True:
    if not find_books():
        break