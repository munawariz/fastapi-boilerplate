from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.database import engine

from article.routes import router as article_router
from article import models as article_model


def get_application():
    try:
        article_model.Base.metadata.create_all(bind=engine)
    except:
        print('Migration Error')
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app

app = get_application()
app.include_router(article_router, prefix="/api/v1/article")