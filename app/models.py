from sqlalchemy import Column, Integer, String

from app.database import Base


class Wine(Base):
    __tablename__ = "WINE"

    wine_id = Column(Integer, primary_key=True, index=True)
    name_kr = Column(String(255), nullable=True)
    name_en = Column(String(255), nullable=True)
    producer = Column(String(255), nullable=True)
    nation = Column(String(255), nullable=True)
    type = Column(String(255), nullable=True)
    sweet = Column(Integer, nullable=True)
    acidity = Column(Integer, nullable=True)
    body = Column(Integer, nullable=True)
    tannin = Column(Integer, nullable=True)
    price = Column(String(255), nullable=True)
    food = Column(String(255), nullable=True)
    pic_url = Column(String(255), nullable=True)
    count = Column(Integer, nullable=False)
    re1 = Column(Integer, nullable=True)
    re2 = Column(Integer, nullable=True)
    re3 = Column(Integer, nullable=True)

    def increase_count(self):
        self.count += 1
        return self
