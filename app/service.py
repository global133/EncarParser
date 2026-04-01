from app.parser import parse_encar
from app.database import save_cars, load_cars
import datetime

def update_cars():
    cars = parse_encar()
    save_cars(cars)
    print(f"[{datetime.datetime.now()}] Cars updated: {len(cars)}")

def get_cars():
    return load_cars()