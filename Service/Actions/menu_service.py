import abc
class Menu_service(abc.ABC):
    @abc.abstractclassmethod
    def get_all_items(self):
        pass
    
    @abc.abstractclassmethod
    def remove_item_from_menu(self, item_id):
        pass
    
    @abc.abstractclassmethod
    def add_item_to_menu(self, json):
        pass