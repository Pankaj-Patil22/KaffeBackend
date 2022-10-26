import Controllers.app as app

class TestMenu:
    def test_respose_status_for_get(self):
        response = app.main().get_app().test_client().get('/getMenu/')
        assert response.status_code == 200
    
    def test_respose_status_for_post(self):
        response = app.main().get_app().test_client().post('/getMenu/')
        assert response.status_code == 405
        
    def test_get_all_menu_items(self):
        response = app.main().get_app().test_client().get('/getMenu/')
        assert response.status_code == 200
        assert {
                    "description": "king fish is for money, so we give it cheap. things are sometimes overrated",
                    "eta": 30,
                    "image": "https://th.bing.com/th/id/OIP.CdqlCxWYa-D_-_02gT5_BQHaF-?pid=ImgDet&rs=1",
                    "item_id": 1,
                    "name": "Not So good Fish",
                    "price": 10,
                    "rating": 4,
                    "serving_size": 1,
                    "veg": False
                } in response.json
