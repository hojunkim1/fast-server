from typing import Union

from pydantic import BaseModel
from typing import List

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
    re1:int
    re2:int
    re3:int

class WineWithRecommendations(BaseModel):
    wine: Wine
    recommendations: List[Wine]