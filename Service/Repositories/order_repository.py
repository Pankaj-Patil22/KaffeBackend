from flask import session
import Models.order as order 
from sqlalchemy.orm import sessionmaker, scoped_session

session = scoped_session(sessionmaker(bind=order.engine))

class OrderRepositry:
    @staticmethod
    def remove_order(order_id):
        order_record = session.query(order.Order).filter_by(order_id=order_id).first()
        session.delete(order_record)
        session.commit()
    
    @staticmethod
    def insert_order_record(special_instructions):
        order_record = order.Order(special_instructions)
        session.add(order_record)
        session.commit()
        if order_record.order_id is None:
            print("Order ID is None error is raised")
            raise Exception("order_id is None")
        return order_record.order_id

    @staticmethod
    def get_order_record (order_id):
        order_record = session.query(order.Order).filter_by(order_id=order_id).first()
        return order_record

    @staticmethod
    def get_special_instruction(order_id):
        order_record = session.query(order.Order).filter_by(order_id=order_id).first()
        return order_record.special_instructions

