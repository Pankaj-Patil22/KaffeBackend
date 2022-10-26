from sqlalchemy import TIMESTAMP,  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.sql import func

engine = create_engine('sqlite:///sqlalchemy.sqlite',echo=True)

base = declarative_base()

class Transaction (base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    table_id = Column(Integer, nullable=True)
    order_id = Column(Integer, nullable=False)
    table_total = Column(Integer, nullable=False)
    order_total = Column(Integer, nullable=False)
    feedback_id = Column(Integer, nullable=True)
    payment_status = Column(Boolean, nullable=True)    
    
    def __init__ (self, user_id, table_id, order_id, table_total, order_total, feedback_id, payment_status):
        self.user_id = user_id
        self.table_id = table_id
        self.order_id = order_id
        self.table_total = table_total
        self.order_total = order_total
        self.feedback_id = feedback_id
        self.payment_status = payment_status
        
base.metadata.create_all(engine)