from  Repositories.menu_repository import MenuRepository
from  Repositories.items_repository import ItemsRepository
from Repositories.feedback_repository import FeedbackRepository
from sqlite3 import Date
from Actions.feedback_service import FeedbackService
from Repositories.transaction_repository import TransactionRepository


class FeedbackServiceImpl(FeedbackService):
    
    def get_items_feedback(self, overall_feedback_id):
        return FeedbackRepository.get_items_feedback_by_feedback_id(overall_feedback_id)
    
    def get_overall_feedback(self, feedback_id):
        return FeedbackRepository.get_feedback_by_id(feedback_id)

    def get_items_in_order(self, order_id):
        items= ItemsRepository.get_all_items_for_order(order_id)
        item_ids=[]
        for item in items:
            item_ids.append(item.item_id)

        menu_items=MenuRepository.get_all_menu_records()
        selected_items=[]
        for menu_item in menu_items:
            if menu_item.item_id in item_ids:
                selected_items.append(menu_item)
        
        response = []
        for item in selected_items:
            response.append({
                "item_id": item.item_id,
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "image": item.image,
                })
        return response

    def add_feedback(self, data):

        order_id=data['order_id']
        order=FeedbackRepository.get_feedback_for_order(order_id)
        if order is not None:
            raise Exception("Feedback already exists for this order")

        overall_rating=data['overall_rating']
        overall_review=data['overall_review']
        items_feedback=data['items_feedback']
        transaction_id=data['transaction_id']
        feedback_id=FeedbackRepository.add_overall_feedback(order_id, overall_rating, overall_review)
        for item in items_feedback:
            item_id=item['item_id']
            rating=item['rating']
            review=item['review']
            item_feedback=FeedbackRepository.add_item_feedback(feedback_id, item_id, rating, review)
        
        TransactionRepository.update_feedback_id(transaction_id, feedback_id)
        return feedback_id
