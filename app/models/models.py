import os
from dataclasses import dataclass
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@dataclass
class Sushi(Base):
    __tablename__ = 'm_sushi'

    id = Column(Integer, primary_key=True)
    sushi_name = Column(String(50), nullable=False)
    category = Column(String(20), nullable=False)
    price = Column(Integer, nullable=False)
    calorie = Column(Integer, nullable=False)

class Db:
    def __init__(self):
        try:
            engine = create_engine(os.environ.get("DATABASE_URL"))
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as e:
            print(f"Failed to connect to database: {e}")
            raise e

    def get_random_sushi_data_within_budget(self, budget):
        try:
            sushi_data = self.session.query(Sushi).filter(Sushi.price <= budget).order_by(func.random()).first()
            return sushi_data
        except SQLAlchemyError as e:
            print(f"Failed get_random_sushi_data_within_budget: {e}")
            raise e

    def calc_min_price(self):
        try:
            min_price = self.session.query(Sushi).order_by(Sushi.price).first()
            return min_price.price
        except SQLAlchemyError as e:
            print(f"Failed calc_min_price: {e}")
            raise e
        
    def get_sushi_datas_within_budget(self, budget):
        # execution query sample:
        # SELECT *
        # FROM m_sushi
        # WHERE id IN (
        #   SELECT id
        #   FROM (
        #     SELECT id, price, SUM(price) OVER (ORDER BY random()) AS running_total
        #     FROM m_sushi
        #   ) AS subquery
        #   WHERE running_total <= 3000
        # );
        try:
            subquery = self.session.query(
                Sushi.id,
                Sushi.price,
                func.sum(Sushi.price).over(order_by=func.random()).label("running_total")
            ).subquery()

            query = self.session.query(Sushi).filter(Sushi.id.in_(
                self.session.query(subquery.c.id).filter(subquery.c.running_total <= budget)
            ))

            result = query.all()
            return result
        except SQLAlchemyError as e:
            print(f"Failed calc_min_price: {e}")
            raise e
