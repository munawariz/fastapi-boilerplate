from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import update
from article.schemas import ArticleCreate as CreateSchema, Article as Schema
from article.models import Article as Model

def get_article(db: Session, article_id: int):
    db_article = db.query(Model).filter(Model.id == article_id).first()
    if db_article:
        return db_article
    else:
        raise HTTPException(status_code=404, detail="Article not found")

def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Model).offset(skip).limit(limit).all()

def create_article(db: Session, article: CreateSchema):
    db_article = Model(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def update_article(db: Session, article_id: int, article: CreateSchema):
    db_article = get_article(db, article_id)
    if db_article:
        db_article.title = article.title
        db_article.body = article.body
        db.commit()
        db.refresh(db_article)
        return db_article
    else: 
        HTTPException(status_code=404, detail="Article not found")

def delete_article(db: Session, article_id: int):
    db_article = get_article(db, article_id)
    if db_article:
        db.delete(db_article)
        db.commit()
        return db_article
    else:
        raise HTTPException(status_code=404, detail="Article not found")