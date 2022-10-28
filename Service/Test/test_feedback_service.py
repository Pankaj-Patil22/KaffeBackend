import Controllers.app as app
import json 

class TestFeedbackService:
    def test_get_items_feedback_valid_reponse_type(self):
        response = app.main().get_app().test_client().get('get_items_in_order/2')
        assert response.status_code == 200
        assert self.is_items_feedback_content_valid(response.get_data(as_text=True), 2) == True 
        
    def test_get_items_in_order_for_get(self):
        response = app.main().get_app().test_client().get('get_items_in_order/1')
        assert response.status_code == 200
    
    def test_get_items_in_order_for_post(self):
        response = app.main().get_app().test_client().post('get_items_in_order/1')
        assert response.status_code == 405
    
    def test_get_items_in_order_for_invalid_id(self):
        response = app.main().get_app().test_client().get('get_items_in_order/0')
        assert response.status_code == 200
        assert response.json == []    
    
    def test_get_items_in_order_valid_reponse_type(self):
        response = app.main().get_app().test_client().get('get_items_in_order/1')
        assert response.status_code == 200
        assert self.is_response_array(response.get_data(as_text=True)) == True 
        
    def test_get_items_in_order_valid_reponse_type(self):
        response = app.main().get_app().test_client().get('get_items_in_order/42')
        assert response.status_code == 200
        assert self.is_content_valid(response.get_data(as_text=True)) == True 
        
    def test_get_overall_feedback_for_get(self):
        response = app.main().get_app().test_client().get('get_overall_feedback/1')
        assert response.status_code == 200
    
    def test_get_overall_feedback_for_post(self):
        response = app.main().get_app().test_client().post('get_overall_feedback/1')
        assert response.status_code == 405
    
    def test_get_overall_feedback_for_invalid_id(self):
        response = app.main().get_app().test_client().get('get_overall_feedback/0')
        assert response.status_code == 404
    
    def test_get_items_in_order_for_content(self):
        id = 2
        response = app.main().get_app().test_client().get('get_overall_feedback/' + str(id))
        assert response.status_code == 200
        assert self.is_feedback_content_valid(response.get_data(as_text=True), id) == True
    
    def test_get_items_feedback_for_get(self):
        response = app.main().get_app().test_client().get('get_items_feedback/2')
        assert response.status_code == 200
    
    def test_get_items_feedback_for_post(self):
        response = app.main().get_app().test_client().post('get_items_feedback/1')
        assert response.status_code == 405
    
    def test_get_items_feedback_for_invalid_id(self):
        response = app.main().get_app().test_client().get('get_items_feedback/0')
        assert response.status_code == 200
        assert response.json == []    
    
    def test_get_items_feedback_valid_reponse_type(self):
        response = app.main().get_app().test_client().get('get_items_in_order/1')
        assert response.status_code == 200
        assert self.is_items_feedback_response_array(response.get_data(as_text=True)) == True 
        
    def test_get_items_feedback_valid_reponse_type(self):
        response = app.main().get_app().test_client().get('get_items_in_order/2')
        assert response.status_code == 200
        assert self.is_items_feedback_content_valid(response.get_data(as_text=True), 2) == True 
        
    
    def is_items_feedback_content_valid(self, data, feedback_id):
        arr = json.loads(data)
        if (len(arr) == 0):
            return False
    
        dic = {}
        for each in arr:
            print("the greatest")
            print(each)
            print(each['feedback_id'])
            print(each['item_id'])
            if (each["feedback_id"] == None or each["feedback_id"] != feedback_id):
                return False
            if (each['item_id'] == None or each['item_id'] == 0 or dic.get(each['item_id']) != None):
                return False
            dic[each['item_id']] = 1
        return True
    
    
    def is_feedback_content_valid(self, data, id):
        return json.loads(data)["feedback_id"] == id
    
    def is_items_feedback_response_array(self, data):
        arr = json.loads(data)
        if (type(arr) == type([])):
            return True
        return False
    
    
    def is_response_array(self, data):
        arr = json.loads(data)
        if (type(arr["prices"]) == type([])):
            return True
        return False
    
    def is_content_valid(self, data):
        arr = json.loads(data)
        if (len(arr) == 0):
            return False
        
        dic = {}
        for each in arr:

            if (each['item_id'] == None or each['item_id'] == 0 or dic.get(each['item_id']) != None):
                return False
            dic[each['item_id']] = 1
        return True