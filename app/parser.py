import requests
from app.config import API_URL
from app.models import Car


import requests

def parse_encar():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # проверяем успешный ответ
        data = response.json()

        cars = []
        items = data.get("SearchResults", [])
        for item in items:
            try:
                car = Car(
                    brand=item.get("Manufacturer"),
                    model=item.get("Model"),
                    year=int(str(item.get("Year"))[:4]) if item.get("Year") else None,
                    mileage=item.get("Mileage"),
                    price=item.get("Price"),
                    images=build_image_url(item)
                )
                cars.append(car)
            except Exception as e:
                print(f"Ошибка при обработке элемента: {e}")

        return cars

    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return []
    except ValueError as e:
        print(f"Ошибка при разборе JSON: {e}")
        return []

def build_image_url(item):
    photos = item.get("Photos")
    phos = []
    if photos:
        for photo in photos:
            result = "https://ci.encar.com" + photo["location"]
            phos.append(result)
        return phos

    return None