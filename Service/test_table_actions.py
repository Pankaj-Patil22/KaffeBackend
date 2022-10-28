from unittest import TestCase
from unittest.mock import patch
from sqlite3 import Date

from Controllers.app import FlaskAppWrapper
from Actions.table_service_impl import TableServiceImpl
from Models.table_model import TableReservations
import Models.table_model as table_model
from Repositories.table_repository import TableRepository
from sqlalchemy.orm import sessionmaker, scoped_session



class TestTableApi(TestCase):

    def setUp(self):
        self.app_wrapper = FlaskAppWrapper()
        self.app_wrapper.app.config['TESTING'] = True
        self.app_wrapper.app.config['DEBUG'] = False
        self.client = self.app_wrapper.app.test_client()
    
    def tearDown(self):
        self.app_wrapper.app.config['TESTING'] = False
        self.app_wrapper.app.config['DEBUG'] = True

    
    def test_get_available_tables_api_successful(self):
        with patch('Actions.table_service_impl.TableServiceImpl.get_available_tables') as mock_get_available_tables:
            reservations={
                "one": '1',
                "two": '1',
                "three": '1',
                "four": '1',
                "five": '1',
                "six": '1',
                "seven": '0',
                "eight": '1',
                "nine": '1',
                "ten": '0',
                "eleven": '1',
                "twelve": '1'   
                }
            mock_get_available_tables.return_value = reservations
            response = self.client.get('/tables/2020/1/1/1')
            expected_response =  {"table_reservation": {
                                "eight": '1',
                                "eleven": '1',
                                "five": '1',
                                "four": '1',
                                "nine": '1',
                                "one": '1',
                                "seven": '0',
                                "six": '1',
                                "ten": '0',
                                "three": '1',
                                "twelve": '1',
                                "two": '1'
                            }
                            }

            self.assertEqual(response.json, expected_response)
            self.assertEqual(response.status_code, 200)

    @patch('Actions.table_service_impl.TableServiceImpl.get_available_tables')
    def test_get_available_tables_api_incorrect_time_slot(self, mock_get_available_tables):
        mock_get_available_tables.return_value = None
        response = self.client.get('/tables/2020/1/1/13')
        self.assertEqual(response.status_code, 400)
    
    @patch('Actions.table_service_impl.TableServiceImpl.get_available_tables')
    def test_get_available_tables_api_incorrect_time_slot2(self, mock_get_available_tables):
        mock_get_available_tables.return_value = None
        response = self.client.get('/tables/2020/1/1/0')
        self.assertEqual(response.status_code, 400)
    
    @patch('Actions.table_service_impl.TableServiceImpl.get_available_tables')
    def test_get_available_tables_api_incorrect_year(self, mock_get_available_tables):
        mock_get_available_tables.return_value = None
        response = self.client.get('/tables/20200/1/1/1')
        self.assertEqual(response.status_code, 400)
    
    @patch('Actions.table_service_impl.TableServiceImpl.get_available_tables')
    def test_get_available_tables_api_incorrect_month(self, mock_get_available_tables):
        mock_get_available_tables.return_value = None
        response = self.client.get('/tables/2020/13/1/1')
        self.assertEqual(response.status_code, 400)

    @patch('Actions.table_service_impl.TableServiceImpl.get_available_tables')
    def test_get_available_tables_api_incorrect_month2(self, mock_get_available_tables):
        mock_get_available_tables.return_value = None
        response = self.client.get('/tables/2020/0/1/1')
        self.assertEqual(response.status_code, 400)

    @patch('Actions.table_service_impl.TableServiceImpl.get_available_tables')
    def test_get_available_tables_api_incorrect_day(self, mock_get_available_tables):
        mock_get_available_tables.return_value = None
        response = self.client.get('/tables/2020/1/32/1')
        self.assertEqual(response.status_code, 400)
    
    @patch('Actions.table_service_impl.TableServiceImpl.get_available_tables')
    def test_get_available_tables_api_incorrect_day2(self, mock_get_available_tables):
        mock_get_available_tables.return_value = None
        response = self.client.get('/tables/2020/1/0/1')
        self.assertEqual(response.status_code, 400)

    @patch('Actions.table_service_impl.TableServiceImpl.get_available_tables')
    def test_get_available_tables_api_invalid(self, mock_get_available_tables):
        mock_get_available_tables.return_value = None
        response = self.client.get('/tables/aaaa/1/1/1/1')
        self.assertEqual(response.status_code, 404)

    

class TestTableActions(TestCase):

    def setUp(self):
        self.table_service = TableServiceImpl()
    
    def tearDown(self):
        pass

    @patch('Repositories.table_repository.TableRepository.get_available_tables')
    def test_get_available_tables_no_entry_in_db(self, mock_get_available_tables):        
        mock_get_available_tables.return_value = None
        date=Date(2020,1,1)
        response = self.table_service.get_available_tables(1,date)
        expected_response =  {'eight':1,'eleven':1,'five':1,'four':1,
                            'nine':1,'one':1,'seven':1,'six':1,
                            'ten':1,'three':1,'twelve':1,'two':1
                            }
        self.assertEqual(response, expected_response)
    
    @patch('Repositories.table_repository.TableRepository.get_available_tables')
    def test_get_available_tables_entry_in_db(self, mock_get_available_tables):
        date=Date(2020,1,1)
        time_slot=1
        reservations=[0 for i in range(10)]
        reservations.extend([1,1])
        mock_get_available_tables.return_value = TableReservations(date,time_slot,reservations)
        
        response = self.table_service.get_available_tables(time_slot,date)
        expected_response =  {'eight':1,'eleven':0,'five':1,'four':1,
                            'nine':1,'one':1,'seven':1,'six':1,
                            'ten':1,'three':1,'twelve':0,'two':1
                            }
        self.assertEqual(response, expected_response)

    @patch('Repositories.table_repository.TableRepository.get_available_tables')
    def test_get_available_tables_booking_full(self, mock_get_available_tables):
        date=Date(2020,1,1)
        time_slot=1
        reservations=[1 for i in range(12)]
        mock_get_available_tables.return_value = TableReservations(date,time_slot,reservations)
        
        response = self.table_service.get_available_tables(time_slot,date)
        expected_response =  {'eight':0,'eleven':0,'five':0,'four':0,
                            'nine':0,'one':0,'seven':0,'six':0,
                            'ten':0,'three':0,'twelve':0,'two':0
                            }
        self.assertEqual(response, expected_response)



class TestTableRepository(TestCase):



    def setUp(self):
        self.table_repository = TableRepository()
        self.session = scoped_session(sessionmaker(bind=table_model.engine))

    def tearDown(self):
        pass

    @patch('Models.table_model.TableReservations', autospec=TableReservations)
    def test_get_available_tables_no_entry_in_db(self, mock_table_reservations):
        date=Date(2022,10,13)
        time_slot=6
        self.session.query(TableReservations).filter(TableReservations.time_slot_id==time_slot, TableReservations.date==date).first().return_value = None
        response = self.table_repository.get_available_tables(time_slot,date)
        self.assertEqual(response, None)










    @patch('Actions.tables_service.TableService')
    def test_table_actions_get_available_tables(self, mock_table_service):
        mock_service = mock_table_service()

        mock_service.get_available_tables.return_value = [
        ]

        response = mock_service.get_available_tables()
        self.assertIsNotNone(response)
        self.assertIsInstance(response, list)


    @patch('Repositories.table_repository.TableRepository')
    def test_table_repository_get_available_tables(self, mock_table_repository):
        mock_repository = mock_table_repository()

        mock_repository.insert_table_reservations.return_value = [1,2]

        date=Date(2020, 12, 12)
        time_slot_id=1
        reservations_table=[0 for i in range(11)]
        reservations_table.append(1)

        response = mock_repository.insert_table_reservations()
        self.assertIsNotNone(response)
        self.assertIsInstance(response, list)