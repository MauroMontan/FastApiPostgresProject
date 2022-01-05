from fastapi import FastAPI
from app.database.database import create_db
from app.config.routes import initRoutes
from app.config.cors import initCors


app = FastAPI(
    title="Your api title"
)

create_db()
initCors(app)
initRoutes(app)
