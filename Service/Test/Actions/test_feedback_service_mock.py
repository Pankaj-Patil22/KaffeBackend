from unittest import TestCase
from unittest.mock import patch

class Feedback_Mock():
    def __init__(self):
        pass

    def get_items_in_order(self, order_id):
        pass

    def add_feedback(self, data):
        pass
    
    def get_overall_feedback(self, feedback_id):
        pass
    
    def get_items_feedback(self, overall_feedback_id):
        pass
    
    def get_items_in_order(self, order_id):
        return [
                {
                    "description": "Chicken Biryani is a South Asian dish with its origins of the Indian subcontinent. It is made with Indian spices, rice, and chicken, and sometimes raisins.",
                    "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/12/chicken-biryani.jpg.webp",
                    "item_id": 15,
                    "name": "Chicken Biryani",
                    "price": 200
                },
                {
                    "description": "Chicken tikka masala is a dish of chunks of roasted marinated chicken in a spiced curry sauce. The sauce is usually creamy and orange-coloured. It is a variation of chicken tikka, a popular starter in Indian cuisine.",
                    "image": "https://cafedelites.com/wp-content/uploads/2018/04/Best-Chicken-Tikka-Masala-IMAGE-1.jpg",
                    "item_id": 16,
                    "name": "Chicken Tikka Masala",
                    "price": 200
                }
            ]

    def get_overall_feedback(self, feedback_id):
        return {
            "overall_rating": 5,
            "overall_comment": "test"
        }

    def add_feedback(self, data):
        return 1
        
    
    def add_feedback(self, data):
        return True

    def get_overall_feedback(self, feedback_id):
        return {
            "feedback_id": 1,
            "overall_rating": 5,
            "overall_comment": "test"
        }
    
    def get_items_feedback(self, overall_feedback_id):
        return [
            {
                "item_id": 1,
                "item_rating": 5,
                "item_comment": "test"
            }
        ]
    

class Test_Feedback_Service(TestCase):
    @patch('Actions.menu_service.FeedbackService')
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