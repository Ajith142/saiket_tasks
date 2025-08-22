import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://www.w3schools.com/html/html_tables.asp"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("h2")
    for i, headline in enumerate(headlines, start=1):
        text = headline.get_text(strip=True)
        print(f"{i}. {text}")

    with open("news_headlines.txt", "w", encoding="utf-8") as f:
        for i, headline in enumerate(headlines, start=1):
            text = headline.get_text(strip=True)
            f.write(f"{i}. {text}\n")
    


if __name__ == "__main__":
    scrape_headlines()
