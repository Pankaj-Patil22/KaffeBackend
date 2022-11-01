from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

engine = create_engine(
    'mysql+mysqlconnector://admin:cafe6789@cafe-database.clcbcurh3gmf.ap-northeast-1.rds.amazonaws.com:3306/cafeDatabase', echo=True)

base = declarative_base()


class Items (base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer)
    item_id = Column(Integer)
    quantity = Column(Integer, nullable=False)

    def __init__(self, order_id, item_id, quantity):
        self.order_id = order_id
        self.item_id = item_id
        self.quantity = quantity


base.metadata.create_all(engine)
