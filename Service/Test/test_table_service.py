import Controllers.app as app

class TestTableService:
    def test_get_available_tables(self):
        response = app.main().get_app().test_client().get('/tables/2022/10/13/1')
        assert response.status_code == 200
    
    def test_get_available_tables_incorrect_time_slot(self):
        response = app.main().get_app().test_client().get('/tables/2022/10/13/13')
        assert response.status_code == 400

    def test_get_available_tables_incorrect_time_slot2(self):
        response = app.main().get_app().test_client().get('/tables/2022/10/13/0')
        assert response.status_code == 400

    def test_get_available_tables_incorrect_year(self):
        response = app.main().get_app().test_client().get('/tables/20224/10/13/1')
        assert response.status_code == 400

    def test_get_available_tables_incorrect_month(self):
        response = app.main().get_app().test_client().get('/tables/2022/102/13/1')
        assert response.status_code == 400
    
    def test_get_available_tables_incorrect_day(self):
        response = app.main().get_app().test_client().get('/tables/2022/10/132/1')
        assert response.status_code == 400
    
    def test_get_available_tables_incorrect_date(self):
        response = app.main().get_app().test_client().get('/tables/2022/10/32/1')
        assert response.status_code == 400

    def test_get_available_tables_incorrect_date2(self):
        response = app.main().get_app().test_client().get('/tables/2022/13/1/1')
        assert response.status_code == 400

    def test_get_available_tables_incorrect_date3(self):
        response = app.main().get_app().test_client().get('/tables/2022/0/1/1')
        assert response.status_code == 400

    def test_get_available_tables_invalid(self):
        response = app.main().get_app().test_client().get('/tables/aaaa/1/13/1')
        assert response.status_code == 404

    def test_get_available_tables_invalid2(self):
        response = app.main().get_app().test_client().get('/tables/2022/12//1')
        assert response.status_code == 404
