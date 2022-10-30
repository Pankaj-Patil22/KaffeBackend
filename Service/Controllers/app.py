from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from threading import Lock
from Actions.menu_service_impl import Menu_service_impl as Menu_service
from sqlite3 import Date
from Actions.table_service_impl import TableServiceImpl as TableService
from Actions.transaction_service_impl import TransactionServiceImpl as TransactionService
from Actions.feedback_service_impl import FeedbackServiceImpl as FeedbackService
import traceback
 
class FlaskAppWrapper():
    lock = Lock()
    def __init__(self):
        self.app = Flask(__name__)
        self._config()
        self._add_services()
        
        @self.app.route('/getTableSessions/', methods = ['GET'])
        def __table_Sessions():
            return self.get_table_sessions()

        @self.app.route('/tables/price', methods=['GET'])
        def __table_Price():
            return self.get_table_prices()

        @self.app.route('/transactionData/', methods=['POST'])
        def __transaction_data():
            return self.transaction_data()

        @self.app.route('/tables/<int:year>/<int:month>/<int:day>/<int:time_slot_id>', methods=['GET'])
        def __available_tables(year, month, day, time_slot_id):
            return self.get_available_tables(year, month, day, time_slot_id)
        
        @self.app.route('/getMenu/', methods = ['GET'])
        def __menu():
            return self.get_Menu()
    
        @self.app.route('/getSuccessfullTransactions/<int:id>', methods = ['GET'])
        def __succeessful_transactions_by_id(id):
            return self.get_successful_transactions_by_id(id)
        
        @self.app.route('/get_items_in_order/<int:order_id>', methods=['GET'])
        def __items_in_order(order_id):
            return self.get_items_in_order(order_id)

        @self.app.route('/feedback/', methods=['POST'])
        def __feedback():
            return self.insert_feedback()
        
        @self.app.route('/get_overall_feedback/<int:id>', methods=['GET'])
        def __get_overall_feedback(id):
            return self.get_overall_feedback(id)
    
        @self.app.route('/get_items_feedback/<int:id>', methods=['GET'])
        def __get_items_feedback(id):
            return self.get_items_feedback(id)
 
        @self.app.route('/remove_transaction/<int:transaction_id>', methods=['GET'])
        def __remove_transaction(transaction_id):
            return self.remove_transaction(transaction_id)
        
        @self.app.route('/remove_item_from_menu/<int:item_id>', methods=['GET'])
        def __remove_item_from_menu(item_id):
            return self.remove_item_from_menu(item_id)
        
        @self.app.route('/add_item_to_menu/', methods=['POST'])
        def __add_item_to_menu():
            return self.add_item_to_menu()
        
        @self.app.route('/getTablesBookedForTransaction/<int:tableId>/<int:transactionId>', methods = ['GET'])
        def __getTablesBookedForTransaction(tableId, transactionId):
            return self.get_tables_booked_for_transaction(tableId, transactionId)
    
        @self.app.route('/getTansactionData/<int:transaction_id>', methods = ['GET'])
        def __getTransactionData(transaction_id):
            return self.get_transaction_data(transaction_id)
    
    def get_transaction_data(self, transaction_id):
        data = self.transaction_service.get_transaction_data(transaction_id)
        data = jsonify(data)
        return data, 200
        
    def get_tables_booked_for_transaction(self, tableId, transactionId):
        tables = self.table_service.get_tables_booked_for_transaction(tableId, transactionId)
        print("\n\n here", tables)
        response = jsonify(tables)
        return response, 200
    
    def remove_item_from_menu(self, item_id):
        self.menu_service.remove_item_from_menu(item_id)
        return jsonify({"success": True}), 200
    
    def add_item_to_menu(self):
        json = request.json
        id = self.menu_service.add_item_to_menu(json)
        if (type(id) == int):
            return jsonify({"id": id}), 200
        return jsonify({"failed": True}), 404
    
    def remove_transaction(self, transaction_id):
        self.transaction_service.remove_transaction(transaction_id)
        return jsonify({"success": True}), 200
    
    def get_items_feedback(self, overall_feedback_id):
        items_feedback = self.feedback_service.get_items_feedback(overall_feedback_id)
        arr = []
        for item_feedback in items_feedback:
            arr.append({
                "id": item_feedback.id,
                "feedback_id": item_feedback.feedback_id,
                "item_id": item_feedback.item_id,
                "rating": item_feedback.rating,
                "review": item_feedback.review
            })
        response = jsonify(arr)
        return response
    
    def get_overall_feedback(self, id):
        overall_feedback = self.feedback_service.get_overall_feedback(id)
        
        if (overall_feedback is None):
            return jsonify({}), 404
        
        feedback =  {
            "feedback_id": overall_feedback.id,
            "order_id": overall_feedback.order_id,       
            "rating": overall_feedback.rating,
            "review": overall_feedback.review,
            }
        response = jsonify(feedback)
        return response
    
    def insert_feedback(self):
        if request.method == 'POST':
            data = request.get_json()
            response=self.feedback_service.add_feedback(data) 
            return data, 200

    def get_items_in_order(self, order_id):
        items = self.feedback_service.get_items_in_order(order_id)
        response = jsonify(items)
        return response,200
    
    def get_successful_transactions_by_id(self, id):
        transactions = self.transaction_service.get_all_successful_transactions_by_id(id)
        arr = []
        for transaction in transactions:
            arr.append({
                "transaction_id": transaction.id,
                "user_id": transaction.user_id,
                "created": transaction.created,
                "table_id": transaction.table_id,
                "order_id": transaction.order_id,
                "table_total": transaction.table_total,
                "order_total": transaction.order_total,
                "feedback_id": transaction.feedback_id,
                "payment_status": transaction.payment_status
            })
        response = jsonify(arr)
        return response
    
    def get_app(self):
        return self.app
         
    def _config(self):
        CORS(self.app)
        self.app.secret_key = os.urandom(24)
    
    def _add_services(self):
        self.table_service = TableService()
        self.menu_service = Menu_service()
        self.transaction_service = TransactionService()
        self.feedback_service = FeedbackService()
        
    def get_Menu(self):
        all_items = self.menu_service.get_all_items()
        arr = []
        for item in all_items:
           arr.append({
           "item_id": item.item_id,
           "name": item.name,
           "description": item.description,
           "eta": item.eta,
           "price": item.price,
           "image": item.image,
           "rating": item.rating,
           "veg": item.veg,
           "serving_size": item.serving_size})
        response = jsonify(arr)
        return response       
        
    def get_available_tables(self, year, month, day, time_slot_id):
        if request.method == 'GET':
            if time_slot_id < 1 or time_slot_id > 12 or time_slot_id is None :
                return jsonify({"message": "Invalid time slot id"}), 400
            if len(str(year)) != 4 or year is None:
                return jsonify({"message": "Invalid year"}), 400
            if len((str(month))) > 2 or month is None or month < 1 or month > 12:
                return jsonify({"message": "Invalid month"}), 400
            if len((str(day))) >2 or day is None or day < 1 or day > 31:
                return jsonify({"message": "Invalid day"}), 400
            try:
                date=Date(year,month,day)
                table_reservation=self.table_service.get_available_tables(time_slot_id, date )
            except ValueError:
                return jsonify({"message": "Invalid date"}), 400
            response = jsonify({"table_reservation": table_reservation})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response,200

    def get_table_sessions(self):
        tableSessions = {
            1:"8-9",
            2:"9-10",
            3:"10-11",
            4:"11-12",
            5:"12-13",
            6:"13-14",
            7:"14-15",
            8:"15-16",
            9:"16-17",
            10:"17-18",
            11:"18-19",
            12:"19-20"
        }
        response = jsonify(tableSessions)
        return response 

    def get_table_prices(self):
        price = [1000, 500, 500, 1000, 1000, 500, 500, 1000, 1000, 500, 500, 1000]
        response = jsonify({"prices": price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    def transaction_data(self):
        print("transactionData")
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            try:
                FlaskAppWrapper.lock.acquire()
                msg = self.transaction_service.set_transaction_data(json)
                print(msg)
                print("\n\n\n hitting success  \n\n\n")
                if (type(msg) == int):
                    return jsonify({"success": True, "transaction_id": msg})
                else:
                    return jsonify({"success": False, "error_msg": msg})
                    
            except Exception as e:
                print("\n\n\n  error  \n\n\n" + str(e) + "\n\n\n")
                traceback.print_tb(e.__traceback__)
                return jsonify({"success": False, "error": e.__traceback__})
            finally:
                FlaskAppWrapper.lock.release()
        print("\n\n\n hitting faild  \n\n\n")
        return jsonify({"success": False, "rare case rio de generio": "need to look"})

    def _corsify_actual_response(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    def run(self, debug,  host, port):
        self.app.run(debug=debug, host=host, port=port)


def main():
    app = FlaskAppWrapper()
    app.run(True, host='0.0.0.0', port=5000)
    return app

if __name__ == '__main__':
    main()