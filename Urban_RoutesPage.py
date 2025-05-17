from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import data
from selenium.webdriver.support import expected_conditions as EC
from SMS import retrieve_phone_code


class UrbanRoutesPage:
    # Localizadores de elementos UI
    from_address = (By.ID, 'from')
    to_address = (By.ID, 'to')
    call_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    comfort = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    phone_number_field = (By.CSS_SELECTOR, ".np-button")
    phone_number_input = (By.ID, "np-text")
    close_button = (By.CLASS_NAME, 'close-button')
    number = (By.XPATH, '//*[@id="phone"]')
    next_button = (By.XPATH, '//*[text()="Siguiente"]')
    phone_code = (By.ID, 'code')
    confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    phone_send_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    select_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    payment_method_select = (By.CLASS_NAME, 'pp-text')
    current_payment_method = (By.CLASS_NAME, 'pp-value-text')
    add_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    number_card_input = (By.ID, "number")
    code_card_input = (By.NAME, "code")
    click_add_card = (By.CLASS_NAME, "card-wrapper")
    add_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_button_payment_method = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    message_for_driver = (By.ID, 'comment')
    reqs_body = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]')
    reqs_button = (By.CLASS_NAME, 'reques head')
    blanket_and_scarves = (
    By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    slider = (By.CLASS_NAME, "switch-input")
    ice_cream = (By.CLASS_NAME, 'counter-plus')
    counter_value = (By.CLASS_NAME, 'counter-value')
    quantity_2 = (By.XPATH,
                  '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    order_number = (By.ID, "number>h_180")
    taxi_search_button = (By.CLASS_NAME, 'smart-button')
    order_header_title = (By.CLASS_NAME, 'order-btn-group')
    burger_button = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[3]')
    wait_driver_details = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[3]')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.from_address)
        ).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.to_address)
        ).send_keys(to_address)

    def get_from(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.from_address)
        ).get_property('value')

    def get_to(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.to_address)
        ).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.call_taxi_button)
        ).click()

    def select_comfort_rate(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.comfort)
        ).click()

    def select_number_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.phone_number_field)
        ).click()

    def add_phone_number(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.number)
        ).send_keys(data.phone_number)

    def the_next_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.next_button)
        ).click()

    def code_number(self):
        phone_code = retrieve_phone_code(driver=self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.phone_code)
        ).send_keys(phone_code)

    def send_cell_info(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_button)
        ).click()

    def fill_phone_number(self):
        self.select_number_button()
        self.add_phone_number()
        self.the_next_button()
        self.code_number()
        self.send_cell_info()

    def pay_click(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.payment_method_select)
        ).click()

    def add_click(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_card)
        ).click()

    def click_card(self):
        card_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.number_card_input)
        )
        card_input.click()
        card_input.send_keys("1234 4321 1408")

    def add_code_card(self):
        code_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.code_card_input)
        )
        code_input.click()
        code_input.send_keys("12" + Keys.TAB)

    def card_submit_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_button)
        ).click()

    def close_button_payment(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.close_button_payment_method)
        ).click()

    def payment_click(self):
        self.pay_click()
        self.add_click()
        self.click_card()
        self.add_code_card()
        self.card_submit_button()
        self.close_button_payment()

    def get_card(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.add_card)
        )

    def write_drive_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.message_for_driver)
        ).send_keys('A continuación puede agregar productos i/o servicios')

    def get_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.message_for_driver)
        ).get_property('value')

    def request_blanket_and_scarves(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.blanket_and_scarves)
        ).click()

    def slider_verification(self):
        slider = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.slider)
        )
        return slider[0].get_property('checked')

    def request_ice_cream(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ice_cream)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.counter_value)
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.quantity_2)
        ).click()

    def get_ice_cream_counter(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ice_cream)
        ).get_property('value')

    def search_taxi(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.taxi_search_button)
        ).click()

    def order_header(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.order_header_title)
        ).click()

    def click_burger_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.burger_button)
        ).click()

    def details_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.wait_driver_details)
        ).click()

    def get_details(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.wait_driver_details)
        ).text
