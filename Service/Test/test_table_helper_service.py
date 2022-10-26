import Controllers.app as app
import json

class TestTableHelper:
    def test_table_session_for_get(self):
        response = app.main().get_app().test_client().get('/getTableSessions/')
        assert response.status_code == 200
        
    def test_table_session_for_post(self):
        response = app.main().get_app().test_client().post('/getTableSessions/')
        assert response.status_code == 405
    
    def test_table_session_not_array(self):
        response = app.main().get_app().test_client().get('/getTableSessions/')
        assert response.status_code == 200
        assert self.is_json_type_arr(response.get_data(as_text=True)) == False
    
    def test_table_session_content(self):
        response = app.main().get_app().test_client().get('/getTableSessions/')
        assert response.status_code == 200
        assert self.is_table_session_data_valid(response.get_data(as_text=True)) == True
        
    def test_table_price_for_get(self):
        response = app.main().get_app().test_client().get('/tables/price')
        assert response.status_code == 200
    
    def test_table_price_for_post(self):
        response = app.main().get_app().test_client().post('/tables/price')
        assert response.status_code == 405

    def test_price_for_array(self):
        response = app.main().get_app().test_client().get('/tables/price')
        assert response.status_code == 200
        assert self.is_price_type_arr(response.get_data(as_text=True)) == True
    
    def test_price_for_array(self):
        response = app.main().get_app().test_client().get('/tables/price')
        assert response.status_code == 200
        assert self.is_price_data_valid(response.get_data(as_text=True)) == True
        
    def is_price_data_valid(self, data):
        json_data = json.loads(data)
        prices = json_data['prices']
        return prices != None and len(prices) == 12
    
    def is_price_type_arr(self, data):
        arr = json.loads(data)
        if (type(arr["prices"]) == type([])):
            return True
        return False
    
    def is_json_type_arr(self, data):
        arr = json.loads(data)
        if (type(arr) == type([])):
            return True
        return False
    
    def is_table_session_data_valid(self, data):
        arr = json.loads(data)
        if (len(arr) == 0):
            return False
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
        
        for key, value in arr.items():
            if (int(key) not in tableSessions.keys() or value != tableSessions[int(key)]):
                return False
        return True