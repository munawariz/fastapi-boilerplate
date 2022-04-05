from fastapi import APIRouter
from article.controllers import get_articles, get_article, post_article, update_article, delete_article

router = APIRouter()

router.add_api_route("/", get_articles, methods=["GET"])
router.add_api_route("/{article_id}", get_article, methods=["GET"])
router.add_api_route("/", post_article, methods=["POST"])
router.add_api_route("/{article_id}", update_article, methods=["PATCH"])
router.add_api_route("/{article_id}", delete_article, methods=["DELETE"])