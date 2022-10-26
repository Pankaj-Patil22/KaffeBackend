import abc

class FeedbackService(abc.ABC):
    @abc.abstractclassmethod
    def get_items_in_order(self, order_id):
        pass

    @abc.abstractclassmethod
    def add_feedback(self, data):
        pass
    
    @abc.abstractclassmethod
    def get_overall_feedback(self, feedback_id):
        pass
    
    @abc.abstractclassmethod
    def get_items_feedback(self, overall_feedback_id):
        pass