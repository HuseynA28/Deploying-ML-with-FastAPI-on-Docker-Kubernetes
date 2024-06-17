from pydantic import BaseModel


class Iris(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

    class Config:
        schema_extra = {
            "example": {
                "SepalLengthCm": 5.1,
                "SepalWidthCm": 3.5,
                "PetalLengthCm": 1.4,
                "PetalWidthCm": 0.2,
            }
        }


class Advertising(BaseModel):
    TV: float
    Radio: float
    Newspaper: float

    class Config:
        schema_extra = {
            "example": {
                "TV": 230.1,
                "Radio": 37.8,
                "Newspaper": 69.2,
            }
        }
