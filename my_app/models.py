from sqlalchemy import Column, String, Boolean, DateTime, Integer, Float, ForeignKey, Enum
from my_app import db
from datetime import datetime


class Category(db.Model):
    __tablename__ = "Category"
    __table_args__ = {'extend_existing': True}
    Id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    Name = db.Column(db.NVARCHAR(length=200), nullable=False)
    Code = db.Column(db.NCHAR(length=200), nullable=False)
    Active = db.Column(db.Integer(), nullable=False)


class Manhwa(db.Model):
    __tablename__ = "Manhwa"
    __table_args__ = {'extend_existing': True}
    Id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    UrlImageManhwa = db.Column(db.NCHAR(length=300), nullable=False)
    UrlCoverImage = db.Column(db.NCHAR(length=300), nullable=True)
    Name = db.Column(db.NVARCHAR(length=300), nullable=False)
    Author = db.Column(db.NVARCHAR(length=500), nullable=True)
    Category = db.Column(db.NVARCHAR(length=300), nullable=True)
    Description = db.Column(db.NVARCHAR(length=4000), nullable=False)
    Create_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    Views = db.Column(db.Integer(), nullable=False)
    Likes = db.Column(db.Integer(), nullable=False)


class Chapter(db.Model):
    __tablename__ = "Chapter"
    __table_args__ = {'extend_existing': True}
    Id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    IdManhwa = Column(Integer, ForeignKey(Manhwa.Id), nullable=False)
    Manhwa = db.relationship('Manhwa', backref='chapter', lazy=False)
    Name = db.Column(db.NVARCHAR(length=300), nullable=False)
    Create_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    HightLightChapter = db.Column(db.Integer(), nullable=False)
    Views = db.Column(db.Integer(), nullable=False)


class UrlImageManhwa(db.Model):
    __tablename__ = "UrlImageManhwa"
    __table_args__ = {'extend_existing': True}
    Id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    IdChapter = Column(Integer, ForeignKey(Chapter.Id), nullable=False)
    Chapter = db.relationship('Chapter', backref='urlimagemanhwa', lazy=False)
    UrlImage = db.Column(db.VARCHAR(length=7800), nullable=False)


if __name__ == "__main__":
    db.create_all()
