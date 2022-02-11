import requests
from bs4 import BeautifulSoup
from utils import Add_Chapter, Add_UrlImageManhwa

if __name__ == '__main__':
    address_website = input('Enter Url Website Crawl: ')
    idManhwa = input('Enter IdManhwa: ')
    print(address_website)
    print(idManhwa)

    content = requests.get(address_website, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"}).content
    soup = BeautifulSoup(content, 'html.parser')
    print("Get Url Chapter")
    listNameChapter = []
    chapter = soup.findAll("div", {"class": "col-xs-5 chapter"})

    listUrl = []
    countUrl = 0
    for i in chapter:
        item = i.find("a")
        listUrl.append(item['href'])
        listNameChapter.append(item.text.strip())
        countUrl += 1

    listNameChapter.reverse()
    listUrl.reverse()
    for index in range(countUrl):
        countDropLine = 0
        idChapter = Add_Chapter(idManhwa, listNameChapter[index])
        address_website = listUrl[index]
        content = requests.get(address_website, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"}).content
        soup = BeautifulSoup(content, 'html.parser')
        colorName = soup.findAll("img", {"class": "lazyload"})
        url = "|"
        for item in colorName:
            try:
                countDropLine += 1
                url += (item['data-src'] + "|")
                if countDropLine > 55:
                    print(url)
                    Add_UrlImageManhwa(url, idChapter, listNameChapter[index])
                    url = "|"
                    countDropLine = 0
            except:
                continue
        if url != "|":
            print(url)
            Add_UrlImageManhwa(url, idChapter, listNameChapter[index])
        url = "|"