from flask import Flask, request, render_template, redirect, url_for, flash
from my_app import app, db
from my_app.models import *
from sqlalchemy import desc
from my_app.utils import EncodeUrlImage, GetChapter
import pyodbc


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/home", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def home():
    listTop9ComicUpdate = Manhwa.query.order_by(desc(Manhwa.Create_date)).limit(9).all()
    listTop6ComicTrendingNow = Manhwa.query.order_by(desc(Manhwa.Views)).limit(6).all()
    return render_template("home.html", listTop6ComicTrendingNow=listTop6ComicTrendingNow,
                           listTop9ComicUpdate=listTop9ComicUpdate)


@app.route("/comic")
def Comic():
    id = request.args.get('id')
    getComic = Manhwa.query.filter_by(Id=id).first()
    getChapter = Chapter.query.filter_by(IdManhwa=getComic.Id)
    countChapter = 0
    for item in getChapter:
        countChapter += 1
    size = 0
    if countChapter > 1:
        getChapter = getChapter[::-1]
        size = countChapter - 1
    return render_template("details_comic.html", comic=getComic, chapter=getChapter, size=size)


@app.route("/comic/<id>", methods=["GET"])
def DetailsComic(id):
    return redirect(url_for('Comic', id=id))


@app.route("/read/comic/<id_chapter>", methods=["GET"])
def DetailsChapter(id_chapter):
    return redirect(url_for('ChapterComic', id=id_chapter))


@app.route("/read-comic-chapter")
def ChapterComic():
    id = request.args.get('id')
    getChapter = Chapter.query.filter_by(Id=id).first()
    getManhwa = Manhwa.query.filter_by(Id=getChapter.IdManhwa).first()
    getListChapter = Chapter.query.filter_by(IdManhwa=getManhwa.Id)

    previous_chapter = getChapter
    next_chapter = getChapter

    size = 0
    for item in getListChapter:
        size += 1

    count = 0
    for item in getListChapter:
        if item.Id == getChapter.Id:
            if 0 < count < size - 1:
                previous_chapter = GetChapter(getListChapter, count - 1)
                next_chapter = GetChapter(getListChapter, count + 1)
            elif count == 0 and count < size - 1:
                previous_chapter = getChapter
                next_chapter = GetChapter(getListChapter, count + 1)
            elif count == size - 1 and count > 0:
                previous_chapter = GetChapter(getListChapter, count - 1)
                next_chapter = getChapter
            else:
                continue
        count += 1

    countUrl = 0;
    getInfoChapter = UrlImageManhwa.query.filter_by(IdChapter=id)
    for item in getInfoChapter:
        countUrl += 1
    listUrlImage = EncodeUrlImage(getInfoChapter)
    return render_template("details_chapter.html", manhwa=getManhwa, chapter=getChapter, listChapter=getListChapter,
                           size=countUrl, listUrlImage=listUrlImage, next_chapter=next_chapter,
                           previous_chapter=previous_chapter)


@app.route('/comic-page=<int:page>', methods=['GET'])
def view(page=1):
    per_page = 18
    posts = Manhwa.query.order_by(Manhwa.Create_date.desc()).paginate(page, per_page, error_out=False)
    return render_template('categories.html', posts=posts, page_current=page)


@app.route('/our-blog')
def OurBlog():
    return render_template('blog.html')
