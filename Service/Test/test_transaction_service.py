import Controllers.app as app
import ast, json

class TestTransaction:
    def test_respose_status_for_get(self):
        response = app.main().get_app().test_client().get('/transactionData/')
        assert response.status_code == 405
        
    def test_respose_status_for_post(self):
        response = app.main().get_app().test_client().post('/transactionData/')
        assert response.status_code == 200
    
    def test_post_data_success(self):
        a =  {
    "items": [
        {
            "itemId": 3,
            "quantity": 1,
            "price": 10,
            "name": "Not so good Bangdo",
            "totalPrice": 10
        }
    ],
    "table_number": "[\"1\"]",
    "table_time_slot": "undefined",
    "table_time_slot_id": "9",
    "table_date": "2022-10-19",
    "table_total_price": "1000",
    "total_dishes_price": "10",
    "specialInstructions": "None None None"
}
        obj = ast.literal_eval(a)
        response = app.main().get_app().test_client().post('transactionData', data=a, follow_redirects=True)
        assert response.status_code == 200
        assert response.json == {"success": True}
    
    def test_getSuccessfullTransactions_get_method(self):
        response = app.main().get_app().test_client().get('/getSuccessfullTransactions/1')
        assert response.status_code == 200
    
    def test_getSuccessfullTransactions_post_method(self):
        response = app.main().get_app().test_client().post('/getSuccessfullTransactions/1')
        assert response.status_code == 405
    
    def test_getSuccessfullTransactions_content(self):
        response = app.main().get_app().test_client().get('/getSuccessfullTransactions/1')
        assert response.status_code == 200
        assert self.has_user_id(response.get_data(as_text=True)) == True
    
    def test_getSuccessfullTransactions_user_not_exits(self):
        response = app.main().get_app().test_client().get('/getSuccessfullTransactions/0')
        assert response.status_code == 200
        assert self.has_user_id(response.get_data(as_text=True)) == False
    
    def has_user_id(self, data):
        arr = json.loads(data)
        if (len(arr) == 0):
            return False
        for each in arr:
            if each['user_id'] != 1:
                return False
        return True
        