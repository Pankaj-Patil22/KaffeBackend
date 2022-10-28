from flask import session
import Models.table_model as table_model
from sqlalchemy.orm import sessionmaker, scoped_session

session = scoped_session(sessionmaker(bind=table_model.engine))

class TableRepository:
    
    @staticmethod
    def remove_reservations_for_transaction_id(table_id, transaction_id):
        table_record = session.query(table_model.TableReservations).filter_by(id=table_id).first()
        if (table_record.one == transaction_id):
            table_record.one = 0
        if (table_record.two == transaction_id):
            table_record.two = 0
        if (table_record.three == transaction_id):
            table_record.three = 0
        if (table_record.four == transaction_id):
            table_record.four = 0
        if (table_record.five == transaction_id):
            table_record.five = 0
        if (table_record.six == transaction_id):
            table_record.six = 0
        if (table_record.seven == transaction_id):
            table_record.seven = 0
        if (table_record.eight == transaction_id):
            table_record.eight = 0
        if (table_record.nine == transaction_id):
            table_record.nine = 0
        if (table_record.ten == transaction_id):
            table_record.ten = 0
        if (table_record.eleven == transaction_id):
            table_record.eleven = 0
        if (table_record.twelve == transaction_id):
            table_record.twelve = 0
        session.commit()
    
    @staticmethod
    def insert_time_slots(start_time, end_time):
        time_slots = table_model.TimeSlots(start_time, end_time)
        session.add(time_slots)
        session.commit()

    @staticmethod
    def insert_table_reservations(date, time_slot_id, reservations_table) -> int:
        table_reservations = table_model.TableReservations(
            date, time_slot_id, reservations_table)
        session.add(table_reservations)
        session.commit()
        return table_reservations.id

    @staticmethod
    def get_available_tables(slot_id, date):
        tables = session.query(table_model.TableReservations).filter(
            table_model.TableReservations.time_slot_id == slot_id, table_model.TableReservations.date == date).first()
        if tables is None:
            return table_model.TableReservations(date, slot_id,[0 for i in range(12)])
        return tables
    
    @staticmethod
    def insert_reservation(table_number, table_time_slot_id, table_date, transaction_id) -> None:
        if (TableRepository.already_entry_made(table_time_slot_id, table_date)):
            return TableRepository.update_reservation(table_number, table_time_slot_id, table_date, transaction_id)

        else:
            reservation = [
                transaction_id if str(table_number) == '1' else 0,
                transaction_id if str(table_number) == '2' else 0,
                transaction_id if str(table_number) == '3' else 0,
                transaction_id if str(table_number) == '4' else 0,
                transaction_id if str(table_number) == '5' else 0,
                transaction_id if str(table_number) == '6' else 0,
                transaction_id if str(table_number) == '7' else 0,
                transaction_id if str(table_number) == '8' else 0,
                transaction_id if str(table_number) == '9' else 0,
                transaction_id if str(table_number) == '10' else 0,
                transaction_id if str(table_number) == '11' else 0,
                transaction_id if str(table_number) == '12' else 0
            ]
            return TableRepository.insert_table_reservations(table_date, table_time_slot_id, reservation)

    @staticmethod
    def getTableMaking(table_number) -> str:
        table_number = str(table_number)
        if (table_number == '1'):
            return 'one'
        if (table_number == '2'):
            return 'two'
        elif (table_number == '3'):
            return 'three'
        elif (table_number == '4'):
            return 'four'
        elif (table_number == '5'):
            return 'five'
        elif (table_number == '6'):
            return 'six'
        elif (table_number == '7'):
            return 'seven'
        elif (table_number == '8'):
            return 'eight'
        elif (table_number == '9'):
            return 'nine'
        elif (table_number == '10'):
            return 'ten'
        elif (table_number == '11'):
            return 'eleven'
        elif (table_number == '12'):
            return 'twelve'
        else:
            return None

    @staticmethod
    def already_entry_made(table_time_slot_id, table_date) -> bool:
        tables = TableRepository.get_tables(table_time_slot_id, table_date)
        if len(tables) > 0:
            return True
        return False

    @staticmethod
    def get_tables(slot_id, date) -> list:
        tables = session.query(table_model.TableReservations).filter(
            table_model.TableReservations.time_slot_id == slot_id, table_model.TableReservations.date == date).all()
        return tables

    @staticmethod
    def update_reservation(table_number, table_time_slot_id, table_date, transaction_id) -> int:
        tables = TableRepository.get_tables(table_time_slot_id, table_date)
        for t in tables:
            print(t, "\n\n ghghgjhgjh")
            if getattr(t, TableRepository.getTableMaking(str(table_number))) == 0:
                setattr(t, TableRepository.getTableMaking(str(table_number)), str(transaction_id))
                print("got table ")
                session.commit()
                print("returning id")
                return t.id
        print("No table available")
        return -1

    @staticmethod
    def getTableMaking(table_number) -> str:
        table_number = str(table_number)
        if (table_number == '1'):
            return 'one'
        if (table_number == '2'):
            return 'two'
        elif (table_number == '3'):
            return 'three'
        elif (table_number == '4'):
            return 'four'
        elif (table_number == '5'):
            return 'five'
        elif (table_number == '6'):
            return 'six'
        elif (table_number == '7'):
            return 'seven'
        elif (table_number == '8'):
            return 'eight'
        elif (table_number == '9'):
            return 'nine'
        elif (table_number == '10'):
            return 'ten'
        elif (table_number == '11'):
            return 'eleven'
        elif (table_number == '12'):
            return 'twelve'
        else:
            return None

    @staticmethod
    def is_table_available(table, table_time_slot_id, table_date) -> bool:
        tables = TableRepository.get_tables(table_time_slot_id, table_date)
        if (tables is None or len(tables) == 0):
            return True
        for t in tables:
            print(str(t) + " - fu")
            print(table)
            print(TableRepository.getTableMaking(str(table)))
            print(getattr(t, TableRepository.getTableMaking(str(table))))
            if getattr(t, TableRepository.getTableMaking(str(table))) == 0:
                return True
        return False

# #run only once to create the database
# for i in range(8, 20,1):
#     start_time = i
#     end_time = i+1
#     print(start_time, end_time)

#     TableRepository.insert_time_slots(start_time, end_time)