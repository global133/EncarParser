from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.service import get_cars
from app.service import update_cars
from app.scheduler import start_scheduler

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
def startup():
    cars = update_cars();
    start_scheduler()

@app.get("/")
def index(request: Request):
    cars = get_cars()
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={
        "request": request,
        "cars": cars
    }
)