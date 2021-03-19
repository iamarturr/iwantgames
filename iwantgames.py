import requests
from bs4 import BeautifulSoup


def get_number_pages(url: str):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    pages = soup.find("ul", class_="page-numbers").find_all("li")
    page = pages[4].find("a", class_="page-numbers").get_text()
    return page


def main(numbers: int, url: str):
    response = requests.get(f"{url}page/{numbers}/", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all("article", class_="game")

    for item in items:
        img = item.find("img").get("src")
        url = item.find("a", class_="game__img").get("href")
        text = item.find("h2").get_text()
        date = item.find("div", class_="date").get_text()

        result.append({
            "img": img,
            "url": url,
            "text": text,
            "date": date
        })


if __name__ == "__main__":
    headers = {"User-Agent": "Mediapartners-Google"}
    result = []

    link = "https://iwantgames.ru/newgames-pc/"
    number = get_number_pages(link)
    for i in range(1, int(number)):
        main(i, link)

    print(result)
