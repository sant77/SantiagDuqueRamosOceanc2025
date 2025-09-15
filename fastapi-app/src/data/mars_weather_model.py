from sqlalchemy import Column, Integer, String, DateTime, Numeric
from src.data.database import Base
from src.data.database import SessionLocal 
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

def get_mars_weather(filters: dict = None):
    db = SessionLocal()
    try:
        query = db.query(MarsWheater)
        if filters:
            for key, value in filters.items():
                if hasattr(MarsWheater, key):
                    query = query.filter(getattr(MarsWheater, key) == value)
        return [mw.to_json() for mw in query.all()]
    finally:
        db.close()

def upsert_mars_weather(data: dict):
    """
    Actualiza el registro si el sol ya existe, si no, lo inserta.
    """
    db = SessionLocal()
    try:
        sol_value = data.get("sol")
        mars_weather = db.query(MarsWheater).filter(MarsWheater.sol == sol_value).first()
        if mars_weather:
            # Update existing record
            for key, value in data.items():
                if hasattr(mars_weather, key):
                    setattr(mars_weather, key, value)
            db.commit()
            db.refresh(mars_weather)
            return mars_weather
        else:
            # Insert new record
            mars_weather = MarsWheater(**data)
            db.add(mars_weather)
            db.commit()
            db.refresh(mars_weather)
            print(f"Inserted new record for sol {sol_value}")
            return mars_weather
    except IntegrityError as e:
        db.rollback()
        print(f"Error de integridad: {e}")
        raise e
    finally:
        db.close()
