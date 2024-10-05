import requests
from bs4 import BeautifulSoup


def scrape_stock():
    url = "https://histock.tw/index"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    trs = soup.find(string="加權指數").find_parent("div").find_all("tr")
    datas = []
    for tr in trs:
        data = []
        for th in tr.find_all("th"):

            data.append(th.text.strip())
        for td in tr.find_all("td"):

            data.append(td.text.strip())
        datas.append(data)

    return datas


if __name__ == "_main_":
    print(scrape_stock())
