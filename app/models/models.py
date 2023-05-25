import os
from dataclasses import dataclass
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

@dataclass
class Sushi:
    id: int
    name: str
    category: str
    price: int
    calorie: int

def __init__(self):
    try:
        engine = create_engine(os.environ.get("DATABASE_URL"))
        Session = sessionmaker(bind=engine)
        self.session = Session()
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        raise e

def get_sushi_data(self):
    try:
        sushi_data = self.session.query(Sushi).all()
        return sushi_data
    except SQLAlchemyError as e:
        print(f"Failed to insert or update data: {e}")
        raise e
