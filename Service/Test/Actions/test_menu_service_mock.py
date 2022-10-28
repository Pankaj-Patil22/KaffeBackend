from unittest import TestCase
from unittest.mock import patch

class Menu_Repository_Mock():
    def __init__(self):
        self.menu = [
        {
          "description": "Chicken Biryani is a South Asian dish with its origins of the Indian subcontinent. It is made with Indian spices, rice, and chicken, and sometimes raisins.",
          "eta": 30,
          "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/12/chicken-biryani.jpg.webp",
          "item_id": 1,
          "name": "Chicken Biryani",
          "price": 200,
          "rating": 4,
          "serving_size": 1,
          "veg": False
        },
        {
          "description": "Chicken tikka masala is a dish of chunks of roasted marinated chicken in a spiced curry sauce. The sauce is usually creamy and orange-coloured. It is a variation of chicken tikka, a popular starter in Indian cuisine.",
          "eta": 30,
          "image": "https://cafedelites.com/wp-content/uploads/2018/04/Best-Chicken-Tikka-Masala-IMAGE-1.jpg",
          "item_id": 2,
          "name": "Chicken Tikka Masala",
          "price": 200,
          "rating": 4,
          "serving_size": 1,
          "veg": False
        },
        {
          "description": "Chicken wings are a type of finger-licking food that is typically served as an appetizer at restaurants, bars, and parties because they are easy to prepare in large batches. Chicken wings are always sold with skin on and bone in because it is hard to remove skin or bone from the wings, otherwise, you will mess things up.",
          "eta": 30,
          "image": "https://3.bp.blogspot.com/-tRx07CaQRaQ/UXYX8V7bHNI/AAAAAAAAJ7s/Eyw2JD0hknY/s1600/BuffaloWings.jpg",
          "item_id": 3,
          "name": "chicken wings",
          "price": 200,
          "rating": 5,
          "serving_size": 2,
          "veg": False
        }
    ]
        self.item_id = 4
        
    def get_all_items(self):
        return self.menu
    
    def remove_item_from_menu(self, item_id):
        for item in self.menu:
            if item['item_id'] == item_id:
                self.menu.remove(item)
                return True
        raise Exception("Item not found")
    
    def add_item_to_menu(self, json):
        self.menu.append({
                        "item_id": self.raise_exception_if_empty(self.item_id),
                        "name": self.raise_exception_if_empty(json['name']),  
                        "description": self.raise_exception_if_empty(json['description']),
                        "eta":30,
                        "price": self.raise_exception_if_empty(json['price']),
                        "image": self.raise_exception_if_empty(json['image']),
                        "rating": 5,
                        "veg": True,
                        "serving_size": 2
                        })
        self.item_id += 1
        return self.item_id - 1
        
    def raise_exception_if_empty(self, data):
        if type(data) == str and len(data) == 0:
            raise Exception("Empty")
        if type(data) == int and data == None:
            raise Exception("Empty")
    
def get_all_items_mock():
    return [
        {
          "description": "Chicken Biryani is a South Asian dish with its origins of the Indian subcontinent. It is made with Indian spices, rice, and chicken, and sometimes raisins.",
          "eta": 30,
          "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/12/chicken-biryani.jpg.webp",
          "item_id": 1,
          "name": "Chicken Biryani",
          "price": 200,
          "rating": 4,
          "serving_size": 1,
          "veg": False
        },
        {
          "description": "Chicken tikka masala is a dish of chunks of roasted marinated chicken in a spiced curry sauce. The sauce is usually creamy and orange-coloured. It is a variation of chicken tikka, a popular starter in Indian cuisine.",
          "eta": 30,
          "image": "https://cafedelites.com/wp-content/uploads/2018/04/Best-Chicken-Tikka-Masala-IMAGE-1.jpg",
          "item_id": 2,
          "name": "Chicken Tikka Masala",
          "price": 200,
          "rating": 4,
          "serving_size": 1,
          "veg": False
        },
        {
          "description": "Chicken wings are a type of finger-licking food that is typically served as an appetizer at restaurants, bars, and parties because they are easy to prepare in large batches. Chicken wings are always sold with skin on and bone in because it is hard to remove skin or bone from the wings, otherwise, you will mess things up.",
          "eta": 30,
          "image": "https://3.bp.blogspot.com/-tRx07CaQRaQ/UXYX8V7bHNI/AAAAAAAAJ7s/Eyw2JD0hknY/s1600/BuffaloWings.jpg",
          "item_id": 3,
          "name": "chicken wings",
          "price": 200,
          "rating": 5,
          "serving_size": 2,
          "veg": False
        }
    ]    
        
class Test_Menu_Service(TestCase):
    @patch('Actions.menu_service.Menu_service')
    def test_output_type(self, mock_menu_service):
        mock_service = mock_menu_service()

        mock_service.get_all_items.return_value = [
        ]
        
        response = mock_service.get_all_items()
        self.assertIsNotNone(response)
        self.assertIsInstance(response, list)
    
    @patch('Actions.menu_service.Menu_service', side_effect=get_all_items_mock)
    def test_menu_content(self, get_all_items):
            self.assertIsNotNone(get_all_items())
            items = get_all_items()
            i = 1
            for item in items:
                self.assertEqual(item["item_id"], i)
                i += 1
    
    @patch('Actions.menu_service.Menu_service', side_effect=Menu_Repository_Mock)
    def test_remove_item_from_menu_invalid_item_id(self, menu_service_obj):
        obj = menu_service_obj()
        self.assertRaises(Exception, obj.remove_item_from_menu, -1)
    
    @patch('Actions.menu_service.Menu_service', side_effect=Menu_Repository_Mock)
    def test_remove_item_from_menu_valid_item_id(self, menu_service_obj):
        obj = menu_service_obj()
        self.assertTrue(obj.remove_item_from_menu(1))
    
    @patch('Actions.menu_service.Menu_service', side_effect=Menu_Repository_Mock)
    def test_remove_item_from_menu_valid_item_id_remove_twice(self, menu_service_obj):
        obj = menu_service_obj()
        item_id = 1
        self.assertTrue(obj.remove_item_from_menu(item_id))
        self.assertRaises(Exception, obj.remove_item_from_menu, item_id)
    
    @patch('Actions.menu_service.Menu_service', side_effect=Menu_Repository_Mock)
    def test_add_item_to_menu_empty_name(self, menu_service_obj):
        obj = menu_service_obj()
        self.assertRaises(Exception, obj.add_item_to_menu, {"name": "", "description": "test", "price": 200, "image": "test"})
    
    @patch('Actions.menu_service.Menu_service', side_effect=Menu_Repository_Mock)
    def test_add_item_to_menu_empty_description(self, menu_service_obj):
        obj = menu_service_obj()
        self.assertRaises(Exception, obj.add_item_to_menu, {"name": "test", "description": "", "price": 200, "image": "test"})
    
    @patch('Actions.menu_service.Menu_service', side_effect=Menu_Repository_Mock)
    def test_add_item_to_menu_empty_price(self, menu_service_obj):
        obj = menu_service_obj()
        self.assertRaises(Exception, obj.add_item_to_menu, {"name": "test", "description": "test", "price": "", "image": "test"})
    
    @patch('Actions.menu_service.Menu_service', side_effect=Menu_Repository_Mock)
    def test_add_item_to_menu_empty_image(self, menu_service_obj):
        obj = menu_service_obj()
        self.assertRaises(Exception, obj.add_item_to_menu, {"name": "test", "description": "test", "price": 200, "image": ""})
    
    @patch('Actions.menu_service.Menu_service', side_effect=Menu_Repository_Mock)
    def test_add_item_to_menu(self, menu_service_obj):
        obj = menu_service_obj()
        item_id = obj.add_item_to_menu({"name": "test", "description": "test", "price": 200, "image": "test"})
        self.assertIsInstance(item_id, int)
        self.assertTrue(item_id > 0)
    
    @patch('Actions.menu_service.Menu_service', side_effect=Menu_Repository_Mock)
    def test_add_item_to_menu_stored(self, menu_service_obj):
        obj = menu_service_obj()
        item_id = obj.add_item_to_menu({"name": "test", "description": "test", "price": 200, "image": "test"})
        all_items = obj.get_all_items()
        for item in all_items:
            if item["item_id"] == item_id:
                self.assertEqual(item["name"], "test")
                self.assertEqual(item["description"], "test")
                self.assertEqual(item["price"], 200)
                self.assertEqual(item["image"], "test")
                
    

    
    