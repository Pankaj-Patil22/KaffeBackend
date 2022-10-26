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
