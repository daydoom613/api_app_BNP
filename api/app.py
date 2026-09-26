from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.routes.endpoints import router

app = FastAPI(title="FinOps Web Foundation", version="1.0.0")
app.include_router(router)

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def homepage():
    return Path(__file__).with_name("index.html").read_text(encoding="utf-8")
