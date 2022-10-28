from sqlalchemy import  VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean

engine = create_engine(
    'mysql+mysqlconnector://admin:qwertyuiop1234567890@kaffedb.clk3x3tl9lw0.ap-south-1.rds.amazonaws.com:3306/sqlalchemy', echo=True)

base = declarative_base()


class Menu (base):
    __tablename__ = 'menu'

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100), nullable=False)
    description = Column(VARCHAR(500), nullable=False)
    eta = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    image = Column(VARCHAR(200), nullable=False)
    rating = Column(Integer, nullable=False)
    veg = Column(Boolean, nullable=False)
    serving_size = Column(Integer, nullable=False)

    def __init__(self, name, description, eta, price, image, rating, veg, serving_size):
        self.name = name
        self.description = description
        self.eta = eta
        self.price = price
        self.image = image
        self.rating = rating
        self.veg = veg
        self.serving_size = serving_size


base.metadata.create_all(engine)
