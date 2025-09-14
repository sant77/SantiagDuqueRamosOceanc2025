from sqlalchemy import Column, Integer, String, Float, DateTime, Numeric
from sqlalchemy.orm import relationship, joinedload
from database import Base
from database import SessionLocal as db
from sqlalchemy.exc import IntegrityError

class MarsWheater(Base):
    __tablename__ = "mars_weather"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sol = Column(Integer, nullable=False)
    average_temperature = Column(Numeric(10, 2), nullable=True, )
    max_temperature = Column(Numeric(10, 2), unique=True, index=True, nullable=False)
    min_temperature = Column(Numeric(10, 2), nullable=True)
    season = Column(String(100), nullable=True)
    month_ordinal = Column(Integer, nullable=True)
    date_start = Column(DateTime, nullable=True)
    date_end = Column(DateTime, nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "sol": self.sol,
            "average_temperature": self.average_temperature,
            "max_temperature": self.max_temperature,
            "min_temperature": self.min_temperature,
            "season": self.season,
            "month_ordinal": self.month_ordinal,
            "date_start": self.date_start,
            "date_end": self.date_end
        }


def insert_mars_weather(user:dict):
    pass
    

def select_mars_weather(address:dict):
    pass
