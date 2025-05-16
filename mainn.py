import data
from selenium import webdriver
from Urban_RoutesPage import UrbanRoutesPage


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):  # Configurar las opciones del navegador
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.driver.implicitly_wait(10)
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_select_comfort_rate(self):
        self.driver.implicitly_wait(10)
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_comfort_rate()
        comfort_status = self.routes_page.select_comfort_rate()
        assert comfort_status == comfort_status

    # Rellenar el número de teléfono
    def test_fill_phone_number(self):
        self.driver.implicitly_wait(10)
        self.routes_page.select_number_button()
        self.routes_page.add_phone_number()
        self.routes_page.the_next_button()
        self.routes_page.code_number()
        self.routes_page.send_cell_info()
        phone_code = data.phone_code
        assert phone_code == phone_code

       # Agregar una tarjeta de crédito
    def test_payment_click(self):
        self.driver.implicitly_wait(10)
        self.routes_page.pay_click()
        self.routes_page.add_click()
        self.routes_page.click_card()
        self.routes_page.add_code_card()
        self.routes_page.card_submit_button()
        self.routes_page.close_button_payment()
        payment_method_select = self.routes_page.get_card()
        assert self.routes_page.get_card() == payment_method_select

    # Escribir un mensaje para el conductor
    def test_write_driver(self):
        self.driver.implicitly_wait(10)
        self.routes_page.write_drive_message()
        assert self.routes_page.get_message() == 'A continuación puede agregar productos i/o servicios '

    # Pedir una manta y pañuelos
    def test_request_blanket_and_scarves(self):
        self.driver.implicitly_wait(10)
        self.routes_page.request_blanket_and_scarves()
        assert self.routes_page.slider_verification()

    # Pedir 2 helados
    def test_request_ice_cream(self):
        self.driver.implicitly_wait(10)
        self.routes_page.request_ice_cream()
        request_ice_cream = self.routes_page.get_ice_cream_counter()
        assert self.routes_page.request_ice_cream() == request_ice_cream

    # Buscar un taxi
    def test_search_taxi(self):
        self.driver.implicitly_wait(10)
        self.routes_page.search_taxi()
        self.routes_page.order_header()
        self.routes_page.click_burger_button()
        self.routes_page.details_button()
        self.routes_page.get_details()
        details_button = self.routes_page.get_details()
        assert self.routes_page.get_details() == details_button

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()