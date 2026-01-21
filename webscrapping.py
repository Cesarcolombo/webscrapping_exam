import requests
from bs4 import BeautifulSoup

#url = "https://quotes.toscrape.com/page/1/"
#response = requests.get(url)
#html = response.text

#if response.status_code != 200:
 #   print("erreur: ", response.status_code)


#print(str(type(html)))
#soup = BeautifulSoup(html, "html.parser")
#print(str(type(soup)))


#print(soup)
def creer_soup(url):
    response = requests.get(url)
    html = response.text

    if response.status_code != 200:
        print("erreur: ", response.status_code)
    soup = BeautifulSoup(html, "html.parser")
    return soup



def extraire_sur_une_page(soup):
    quotes = soup.find_all("div", class_="quote")
    tags = []
    citation = []
    for quote in quotes:
        citation .append(quote.find("span", class_="text").get_text())
        tags.append([tag.get_text() for tag in quote.find_all("a", class_="tag")])
    return [(citation[k] , tags[k]) for k in range(len(citation))]
#extraire_sur_une_page(soup)
#print(str(extraire_sur_une_page(soup)))


def extraire_sur_plusieurs_pages(max):
    donnee = []
    k = 1
    while k < max + 1:
        url = f"https://quotes.toscrape.com/page/{k}/"
        soup = creer_soup(url)
        donnee += extraire_sur_une_page(soup)
        k += 1
    return donnee




donnee = extraire_sur_plusieurs_pages(100)

print(donnee[:2])  
import json
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(donnee, f, ensure_ascii=False, indent=4)



def sauvegarder_donnees(donnees):
    pass

