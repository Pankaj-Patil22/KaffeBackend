from sqlalchemy import DATE, TIMESTAMP, VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.sql import func

engine = create_engine(
    'mysql+mysqlconnector://admin:lookslikepassword@kaffe-1.cobmbcmgxtr3.ap-south-1.rds.amazonaws.com:3306/sqlalchemy', echo=True)

base = declarative_base()


class TimeSlots (base):
    __tablename__ = 'time_slots'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_time = Column(VARCHAR(2))
    end_time = Column(VARCHAR(2))

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


class TableReservations (base):
    __tablename__ = 'table_reservations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    date = Column(DATE, nullable=False)
    time_slot_id = Column(Integer, ForeignKey('time_slots.id'))
    one = Column(Integer, default=0)
    two = Column(Integer, default=0)
    three = Column(Integer, default=0)
    four = Column(Integer, default=0)
    five = Column(Integer, default=0)
    six = Column(Integer, default=0)
    seven = Column(Integer, default=0)
    eight = Column(Integer, default=0)
    nine = Column(Integer, default=0)
    ten = Column(Integer, default=0)
    eleven = Column(Integer, default=0)
    twelve = Column(Integer, default=0)

    def __init__(self, date, time_slot_id, reservations):
        self.date = date
        self.time_slot_id = time_slot_id
        self.one = reservations[0]
        self.two = reservations[1]
        self.three = reservations[2]
        self.four = reservations[3]
        self.five = reservations[4]
        self.six = reservations[5]
        self.seven = reservations[6]
        self.eight = reservations[7]
        self.nine = reservations[8]
        self.ten = reservations[9]
        self.eleven = reservations[10]
        self.twelve = reservations[11]


base.metadata.create_all(engine)
