from bs4 import BeautifulSoup
import requests


def webdir(url, depth, indent):
    try:
        if depth > 0:
            print("\t"*indent)
            print(url)
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            links = soup.select("a").attrs["href"]
            for link in links:
                webdir(link, depth-1, indent+1)
    except AttributeError:
        pass
