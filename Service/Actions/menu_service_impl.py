# from menu_service import Menu_service
from Actions.menu_service import Menu_service
from Repositories.menu_repository import MenuRepository
from  sqlalchemy.orm.exc import UnmappedInstanceError
class Menu_service_impl(Menu_service):
    def get_all_items(self):
        return MenuRepository.get_all_menu_records()
    
    def remove_item_from_menu(self, item_id):
        try:
            MenuRepository.remove_item_from_menu(item_id)
            return True
        except UnmappedInstanceError:
            raise Exception("Item not found")
        
    def add_item_to_menu(self, json):
        try:
            return MenuRepository.insert_menu_record(json['name'],
                                          json['description'],
                                          30,
                                          json['price'],
                                          json['image'],
                                          5,
                                          True,
                                          2)
        except Exception as e:
            raise Exception("Error adding item to menu")