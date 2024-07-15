import time
from bs4 import BeautifulSoup
import requests
import yfinance

url = "https://finance.yahoo.com/topic/latest-news/"
links = []

def fetch_data():
    response = requests.get(url)
    return response.text

def extract_link(text):
    soup = BeautifulSoup(text, 'html.parser')
    news_div = soup.find('div', id="mrt-node-Fin-Stream")

    if not news_div:
        print("error")

    content = news_div.find_all('a', href=True)
    for item in content:
        href = item['href']
        if '/news/' in href:
            if href not in links:
                links.append(href)
                print(href)
                write_link_to_file(href)         
    return links


def write_link_to_file(text):
    with open('links.txt', 'a') as file:
        file.write(text)
        file.write('\n')

def print_links(list):
    for link in links:
        print(list)

def main():
    with open('links.txt', 'r') as file: #adds links currently in text file to list to avoid duplicates
        for line in file:
            pruned = line.strip()
            links.append(pruned)

    try:
          while True:
                print("Updating Links:")
                page_content = fetch_data()
                news_links = extract_link(page_content)
                time.sleep(300)
    except Exception as e:
        print("error")

if __name__ == "__main__":
    main()