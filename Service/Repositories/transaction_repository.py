from flask import session
import Models.transaction as transaction
from sqlalchemy.orm import sessionmaker, scoped_session

session = scoped_session(sessionmaker(bind=transaction.engine))

class TransactionRepository:
        
    @staticmethod
    def insert_transaction_record(user_id, order_id, table_total, order_total, payment_status):
        transaction_record = transaction.Transaction(user_id, None, order_id, table_total, order_total, None, payment_status)
        session.add(transaction_record)
        session.commit()
        if transaction_record.id is None:
            raise Exception("transaction_record id is None")
        return transaction_record.id
      
     
    @staticmethod
    def update_table_id(transaction_id, table_id):
        transaction_record = session.query(transaction.Transaction).filter_by(id=transaction_id).first()
        transaction_record.table_id = table_id
        session.commit()
    
    @staticmethod
    def update_feedback_id(transaction_id, feedback_id):
        transaction_record = session.query(transaction.Transaction).filter_by(id=transaction_id).first()
        transaction_record.feedback_id = feedback_id
        session.commit()
    
    @staticmethod
    def update_payment_status(transaction_id, payment_status):
        transaction_record = session.query(transaction.Transaction).filter_by(id=transaction_id).first()
        transaction_record.payment_status = payment_status
        session.commit()
    
    @staticmethod
    def get_all_transactions():
        return session.query(transaction.Transaction).all()
    
    @staticmethod
    def get_all_successful_transactions():
        return session.query(transaction.Transaction).filter_by(payment_status=True).all()
    
    @staticmethod
    def get_all_successful_transactions_by_id(user_id):
        return session.query(transaction.Transaction).filter_by(user_id=user_id, payment_status=True).order_by(transaction.Transaction.created.desc()).all()

    @staticmethod
    def get_transaction_by_id(transaction_id):
        return session.query(transaction.Transaction).filter_by(id=transaction_id).first()
    
    def remove_transaction(transaction_id):
        transaction_record = session.query(transaction.Transaction).filter_by(id=transaction_id).first()
        session.delete(transaction_record)
        session.commit()