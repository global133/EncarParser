from pydantic import BaseModel

class Car(BaseModel):
    brand: str
    model: str
    year: int
    mileage: int
    price: int
    images: list