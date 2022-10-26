from unittest import TestCase
from unittest.mock import patch


class TestBlog(TestCase):
    @patch('Actions.menu_service.Menu_service')
    def test_blog_posts(self, mock_menu_service):
        mock_service = mock_menu_service()

        mock_service.get_all_items.return_value = [
        ]

        response = mock_service.get_all_items()
        self.assertIsNotNone(response)
        self.assertIsInstance(response, list)
