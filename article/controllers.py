from pydantic import UUID4
from article import queries
from article.schemas import ArticleCreate
from app.database import get_db
from fastapi import HTTPException

def get_articles():
    return queries.get_articles(get_db().__next__())

def get_article(article_id: UUID4):
    return queries.get_article(get_db().__next__(), article_id)

def post_article(article: ArticleCreate):
    return queries.create_article(get_db().__next__(), article)

def update_article(article_id: UUID4, article: ArticleCreate):
    return queries.update_article(get_db().__next__(), article_id, article)

def delete_article(article_id: UUID4):
    return queries.delete_article(get_db().__next__(), article_id)