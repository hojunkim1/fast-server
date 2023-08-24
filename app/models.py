from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base


class ToDo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(255), nullable=False)
    is_done = Column(Boolean, nullable=False)

    def done(self):
        self.is_done = True
        return self

    def undone(self):
        self.is_done = False
        return self

    def __repr__(self):
        return f"ToDo(id={self.id}, contents={self.contents}, id_done={self.is_done})"


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

    def increase_count(self):
        self.count += 1
        return self
