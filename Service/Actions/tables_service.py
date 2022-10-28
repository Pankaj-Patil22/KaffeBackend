import abc

class TableService(abc.ABC):
    @abc.abstractclassmethod
    def get_available_tables(self, time_slot_id, date):
        pass
