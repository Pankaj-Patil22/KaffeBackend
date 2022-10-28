from Actions.transaction_service import TransactionService
from  Repositories.table_repository import TableRepository
from  Repositories.order_repository import OrderRepositry
from  Repositories.items_repository import ItemsRepository
from  Repositories.menu_repository import MenuRepository
from  Repositories.transaction_repository import TransactionRepository
from  Repositories.feedback_repository import FeedbackRepository

import json
from sqlite3 import Date

class TransactionServiceImpl(TransactionService):

    def get_all_transactions(self):
        return TransactionRepository.get_all_transactions()
    
    def get_all_successful_transactions(self):
        return TransactionRepository.get_all_successful_transactions()
    
    def get_all_successful_transactions_by_id(self, user_id):
        return TransactionRepository.get_all_successful_transactions_by_id(user_id)

    def remove_transaction(self,transaction_id):
        transaction_record =  TransactionRepository.get_transaction_by_id(transaction_id)
        TransactionRepository.remove_transaction(transaction_id)
        feedback_id = transaction_record.feedback_id
        order_id = transaction_record.order_id
        table_id = transaction_record.table_id
        TableRepository.remove_reservations_for_transaction_id(table_id, transaction_id)
        OrderRepositry.remove_order(order_id)
        ItemsRepository.remove_items(order_id)
        if (feedback_id != None):
            FeedbackRepository.remove_all_items_feedback_for_feedback_id(feedback_id)
            FeedbackRepository.remove_overall_feedback(feedback_id)

    def set_transaction_data(self, json_data):
        print("doing reservation")
        table_numbers = json.loads(json_data["table_number"])
        table_time_slot_id =  json_data["table_time_slot_id"]
        table_date = json_data["table_date"]
        items = json_data["items"]
        special_instructions = json_data["specialInstructions"] 
        table_total = json_data["table_total_price"]
        order_total = json_data["total_dishes_price"]
        
        print("table_numbers", table_numbers)
        print("table_time_slot_id", table_time_slot_id)
        print("table_date", table_date)
        print("items", items)
        print("special_instructions", special_instructions)
        print("table_total", table_total)
        print("order_total", order_total)
               
        if len(table_numbers) == 0 or len(table_numbers) > 12:
            return "incorrect tables selection"
        if table_time_slot_id == None or table_date == None:
            return "Insuffficient table data, slot or date not choosen"
        if len(items) == 0:
            return "items not selected"

        if not self.tables_available(table_numbers, table_time_slot_id, table_date):
            return "reservation failed table not available"
        
        order_id = self.validate_and_store_dishes(items , special_instructions)
        if order_id == False:
            return "order failed"
        
        transaction_id = TransactionRepository.insert_transaction_record(1, order_id, table_total, order_total, False)
        if (transaction_id == False):
            return "transaction failed"
        
        reservation_id = self.validate_and_store_table(table_numbers, table_time_slot_id, table_date, transaction_id)
        if reservation_id == False:
            return "reservation failed"
        
        TransactionRepository.update_table_id(transaction_id, reservation_id)
        TransactionRepository.update_payment_status(transaction_id, True)
        
        return int(transaction_id)
    
    def validate_and_store_table(self, table_numbers, table_time_slot_id, table_date, transaction_id):
        arr = table_date.split("-")
        table_date=Date(int(arr[0]), int(arr[1]), int(arr[2]))
        if not self.tables_available(table_numbers, table_time_slot_id, table_date):
            print("Table not available")
            return False
        
        table_time_slot_id = int(table_time_slot_id)
        
        reservation_id = -1
        
        for table in table_numbers:
            if (len(table) == 0):
                print("Table number not provided", table, "asda")
            print("Table: ", table," whole arr", table_numbers)
            print(f"Table: {table} whole arr {table_numbers}")
            table = int(table)
            reservation_id = TableRepository.insert_reservation(table, table_time_slot_id, table_date, transaction_id)
        return reservation_id

    def tables_available(self, table_numbers, table_time_slot_id, table_date):
        for table in table_numbers:
            if not TableRepository.is_table_available(table, table_time_slot_id, table_date):
                return False
        return True

    def validate_and_store_dishes(self, dishes, specialInstructions):
        print("storing order")
        order_id=OrderRepositry.insert_order_record(specialInstructions)
        print("dishes")
        for dish in dishes:
            print("dish", dish)
            print("dish", dish["itemId"])
            if MenuRepository.get_first_menu_record(dish['itemId']) is None:
                print("Invalid item id")
                return False
            print("calling insert_items_record")
            ItemsRepository.insert_items_record(order_id, dish['itemId'], dish['quantity'])
        return order_id
        
