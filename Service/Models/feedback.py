from sqlalchemy import VARCHAR, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)

base = declarative_base()


class OverallFeedback (base):
    __tablename__ = 'overall_feedback'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id=Column(Integer)
    rating=Column(Integer)
    review=Column(VARCHAR(255))

    def __init__(self, order_id,rating,review):
        self.order_id = order_id
        self.rating = rating
        self.review = review

class ItemFeedback  (base):
    __tablename__ = 'item_feedback'

    id = Column(Integer, primary_key=True, autoincrement=True)
    feedback_id = Column(Integer, ForeignKey ('overall_feedback.id'))
    item_id = Column(Integer)
    rating=Column(Integer)
    review=Column(VARCHAR(255))


    def __init__(self, feedback_id, item_id, rating,review):
        self.feedback_id = feedback_id
        self.item_id = item_id
        self.rating = rating
        self.review = review

base.metadata.create_all(engine)
