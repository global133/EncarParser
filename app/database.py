import json
import os
from app.config import DATA_FILE

def save_cars(cars):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([car.model_dump() for car in cars], f, ensure_ascii=False, indent=2)
        
        print(f"Данные сохранены в {DATA_FILE}")
    except Exception as e:
        print(f"Ошибка сохранения: {e}")

def load_cars():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []