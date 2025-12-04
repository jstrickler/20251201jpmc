from enum import Enum
from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Color(str, Enum):
    red = "red"
    blue = "blue"
    purple = "purple"

class Size(str, Enum):
    small = "small"
    medium = "medium"
    large = "large"

class Animal(BaseModel):
    name: str
    description: str
    sex: str   # M/F
    species: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/food")
async def food():
    return {
        "bread": "bagel",
        "pie": "apple",
        "beverage": "lhassi",
    }


    
@app.get("/items/{item_id}/{color}")
async def read_item(item_id: int, color: Color, size: Size|None=None, animal=None):
    if color == Color.blue:
        code = "Navy"
    else:
        code = "Black"
    return {"item_id": item_id, "color": color, "code": code,
            "size": size, "animal": animal}

@app.get("/items/123/me")
async def get_item():
    return {"msg": "huh???"}

@app.post("/animals", status_code=201)
async def add_animal(animal: Animal):
    return {"status": "new record", "name": animal.name, "description": animal.description}
    # save animal data to DB (or ???)

@app.put("/animals")
async def update_animal(animal: Animal):
        return {"status": "updated", "name": animal.name, "description": animal.description}

@app.get("/animals/{id}")
async def get_animal(id, name: Annotated[str | None, Query(max_length=10)]):
    return {"name": name}