from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestOrderProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')  # replace with your website URL

    def test_order_process(self):
        # Search for a product
        search_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'search_query')))
        search_input.send_keys('book')
        search_input.submit()

        # Add product to cart
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-cart-button']")))
        add_to_cart_button.click()

        # Click "Shopping Cart" from the success popup
        shopping_cart_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Shopping cart')))
        shopping_cart_link.click()

        # Use the "Checkout as Guest" option
        checkout_as_guest_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'checkout-as-guest-button')))
        checkout_as_guest_button.click()

        # Fill out the order form
        first_name_input = self.driver.find_element_by_id('FirstName')
        last_name_input = self.driver.find_element_by_id('LastName')
        email_input = self.driver.find_element_by_id('Email')
        city_input = self.driver.find_element_by_id('City')
        address1_input = self.driver.find_element_by_id('Address1')
        zip_postal_code_input = self.driver.find_element_by_id('ZipPostalCode')
        phone_number_input = self.driver.find_element_by_id('PhoneNumber')
        country_id_input = self.driver.find_element_by_id('CountryId')
        state_province_id_input = self.driver.find_element_by_id('StateProvinceId')
        shipping_option_select = self.driver.find_element_by_css_selector('#shippingoption_1')

        first_name_input.send_keys('Test')
        last_name_input.send_keys('User')
        email_input.send_keys('random_email')
        city_input.send_keys('Riga')
        address1_input.send_keys('Street 1')
        zip_postal_code_input.send_keys('LV-1234')
        phone_number_input.send_keys('12345678')
        country_id_input.send_keys('124')
        state_province_id_input.send_keys('0')
        shipping_option_select.click()

        # Fill out the payment method section
        payment_method_option_button = self.driver.find_element_by_css_selector('#paymentmethod_1')
        payment_method_option_button.click()
        credit_card_type_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'CreditCardType')))
        cardholder_name_input = self.driver.find_element_by_id('CardholderName')
        card_number_input = self.driver.find_element_by_id('CardNumber')
        expire_month_input = self.driver.find_element_by_id('ExpireMonth')
        expire_year_input = self.driver.find_element_by_id('ExpireYear')
        card_code_input = self.driver.find_element_by_id('CardCode')

        credit_card_type_input.send_keys('visa')
        cardholder_name_input.send_keys('Test User')
        card_number_input.send_keys('4111111111111111')
        expire_month_input.send_keys('4')
        expire_year_input.send_keys('2027')
        card_code_input.send_keys('123')

        # Submit the order
        confirm_order_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='confirm-order-button']")))
        confirm_order_button.click()

        # Check for an order completion message
        order_completion_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".order-completed-page .title strong")))
        self.assertEqual(order_completion_message.text, 'Your order has been successfully processed!')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()