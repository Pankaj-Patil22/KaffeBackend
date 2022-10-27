
from sqlalchemy import VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

# engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)
engine = create_engine(
    'mysql+mysqlconnector://admin:qwertyuiop1234567890@kaffedb.clk3x3tl9lw0.ap-south-1.rds.amazonaws.com:3306/sqlalchemy', echo=True)

base = declarative_base()


class Order (base):
    __tablename__ = 'order'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    special_instructions = Column(VARCHAR(500))

    def __init__(self, special_instructions):
        self.special_instructions = special_instructions


base.metadata.create_all(engine)
