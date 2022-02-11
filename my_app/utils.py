from my_app import common
from my_app import db
from my_app.models import Chapter, UrlImageManhwa
from datetime import datetime

def EncodeUrlImage(UrlImageChapter):
    listUrl = []
    for item in UrlImageChapter:
        lengthUrl = len(item.UrlImage)

        url = item.UrlImage
        subString = ""
        for i in range(1, lengthUrl):
            if url[i] == '|' and i != 0:
                listUrl.append(subString)
                subString = ""
            else:
                subString += url[i]
    return listUrl

def GetChapter(ListChapter, index):
    size = 0
    for item in ListChapter:
        if size == index:
            return item
        size += 1

def Add_Chapter(idManhwa, name):
    chapter = Chapter()
    chapter.IdManhwa = idManhwa
    chapter.Name = name
    chapter.Create_date = datetime.now()
    chapter.HightLightChapter = 0
    chapter.Views = 1

    db.session.add(chapter)
    try:
        db.session.commit()
        return chapter.Id
    except:
        return False

def Add_UrlImageManhwa(urlImage, IdChapter, nameChapter):
    urlImageManhwa = UrlImageManhwa()
    urlImageManhwa.IdChapter = IdChapter
    urlImageManhwa.UrlImage = urlImage
    db.session.add(urlImageManhwa)
    try:
        db.session.commit()
        print("Crawl Comic Successful " + nameChapter)
        return True
    except:
        return False