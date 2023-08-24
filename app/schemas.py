from typing import Union

from pydantic import BaseModel


class ToDo(BaseModel):
    id: Union[int, None] = None
    contents: str
    is_done: bool

    class Config:
        from_attributes = True


class OcrItem(BaseModel):
    ocr_text: str


class Wine(BaseModel):
    wine_id: Union[int, None] = None
    name_kr: str
    name_en: str
    producer: str
    nation: str
    type: str
    sweet: int
    acidity: int
    body: int
    tannin: int
    price: str
    food: str
    pic_url: str
    count: int
