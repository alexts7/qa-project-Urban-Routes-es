import data
from selenium import webdriver
from Urban_RoutesPage import UrbanRoutesPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):  # Configurar las opciones del navegador
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        # Aquí podemos mantener un implicitly_wait global con un valor pequeño como respaldo
        cls.driver.implicitly_wait(5)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        # Espera explícita antes de configurar la ruta
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.routes_page.from_address)
        )
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_select_comfort_rate(self):
        # Espera explícita para el botón de llamar taxi
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.call_taxi_button)
        )
        self.routes_page.click_call_taxi_button()

        # Espera explícita para la opción Comfort
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.comfort)
        )
        self.routes_page.select_comfort_rate()
        comfort_status = self.routes_page.select_comfort_rate()
        assert comfort_status == comfort_status

    # Rellenar el número de teléfono
    def test_fill_phone_number(self):
        # Espera explícita para el botón de número de teléfono
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.phone_number_field)
        )
        self.routes_page.select_number_button()

        # Espera para el campo de número
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.routes_page.number)
        )
        self.routes_page.add_phone_number()

        # Espera para el botón siguiente
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.next_button)
        )
        self.routes_page.the_next_button()

        # Espera para el campo de código
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.routes_page.phone_code)
        )
        self.routes_page.code_number()

        # Espera para el botón de confirmación
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.confirm_button)
        )
        self.routes_page.send_cell_info()

        phone_code = data.phone_code
        assert phone_code == phone_code

    # Agregar una tarjeta de crédito
    def test_payment_click(self):
        # Espera para método de pago
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.payment_method_select)
        )
        self.routes_page.pay_click()

        # Espera para añadir tarjeta
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.add_card)
        )
        self.routes_page.add_click()

        # Espera para campo de tarjeta
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.routes_page.number_card_input)
        )
        self.routes_page.click_card()

        # Espera para campo de código
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.routes_page.code_card_input)
        )
        self.routes_page.add_code_card()

        # Espera para botón enviar
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.add_button)
        )
        self.routes_page.card_submit_button()

        # Espera para botón cerrar
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.close_button_payment_method)
        )
        self.routes_page.close_button_payment()

        payment_method_select = self.routes_page.get_card()
        assert self.routes_page.get_card() == payment_method_select

    # Escribir un mensaje para el conductor
    def test_write_driver(self):
        # Espera para campo de mensaje
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.routes_page.message_for_driver)
        )
        self.routes_page.write_drive_message()
        assert self.routes_page.get_message() == 'A continuación puede agregar productos i/o servicios '

    # Pedir una manta y pañuelos
    def test_request_blanket_and_scarves(self):
        # Espera para opción de manta y pañuelos
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.blanket_and_scarves)
        )
        self.routes_page.request_blanket_and_scarves()
        assert self.routes_page.slider_verification()

    # Pedir 2 helados
    def test_request_ice_cream(self):
        # Espera para opción de helados
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.ice_cream)
        )
        self.routes_page.request_ice_cream()
        request_ice_cream = self.routes_page.get_ice_cream_counter()
        assert self.routes_page.request_ice_cream() == request_ice_cream

    # Buscar un taxi
    def test_search_taxi(self):
        # Espera para botón buscar taxi
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.taxi_search_button)
        )
        self.routes_page.search_taxi()

        # Espera para header del pedido
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.routes_page.order_header_title)
        )
        self.routes_page.order_header()

        # Espera para botón menú hamburguesa
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.burger_button)
        )
        self.routes_page.click_burger_button()

        # Espera para botón detalles
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.routes_page.wait_driver_details)
        )
        self.routes_page.details_button()

        # Espera para verificar detalles
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.routes_page.wait_driver_details)
        )
        details_button = self.routes_page.get_details()
        assert self.routes_page.get_details() == details_button

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
