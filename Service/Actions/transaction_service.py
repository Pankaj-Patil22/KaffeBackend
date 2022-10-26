import abc

class TransactionService(abc.ABC):
    @abc.abstractclassmethod
    def set_transaction_data(self, json_data):
        pass