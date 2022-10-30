from Actions.tables_service import TableService
from Models.table_model import TableReservations
from Repositories.table_repository import TableRepository
import DTO.available_table_dto as available_table_dto

class TableServiceImpl(TableService):
    def get_available_tables(self, time_slot_id, date):
        tables = TableRepository.get_available_tables(time_slot_id, date)
        if tables is None:
            reservations=TableReservations(date, time_slot_id,[0 for i in range(12)])
            return available_table_dto.AvailableTableDTO(reservations).__dict__
        return available_table_dto.AvailableTableDTO(tables).__dict__
    
    def get_tables_booked_for_transaction(self, tableId, transactionId):
        tables_record = TableRepository.get_tables_for_tableID(tableId)
        tables = self.get_tables_for_transactionID(tables_record, transactionId)
        return tables

    def get_tables_for_transactionID(self, tables_record, transactionId):
        tables_booked = []
        tables_record = tables_record[0]
        if (tables_record.one == transactionId):
            tables_booked.append(1)
        if (tables_record.two == transactionId):
            tables_booked.append(2)
        if (tables_record.three == transactionId):
            tables_booked.append(3)
        if (tables_record.four == transactionId):
            tables_booked.append(4)
        if (tables_record.five == transactionId):
            tables_booked.append(5)
        if (tables_record.six == transactionId):
            tables_booked.append(6)
        if (tables_record.seven == transactionId):
            tables_booked.append(7)
        if (tables_record.eight == transactionId):
            tables_booked.append(8)
        if (tables_record.nine == transactionId):
            tables_booked.append(9)
        if (tables_record.ten == transactionId):
            tables_booked.append(10)
        if (tables_record.eleven == transactionId):
            tables_booked.append(11)
        if (tables_record.twelve == transactionId):
            tables_booked.append(12)
        
        return tables_booked