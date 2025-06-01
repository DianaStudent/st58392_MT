import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_checkout(self):
        # Open the home page
        self.driver.get("http://max/")

        # Search for a product (e.g. "book")
        search_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'q')))
        search_input.send_keys('book')
        search_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'btnG')))
        search_button.click()

        # Add the first item to cart
        add_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Add to Cart']")))
        add_cart_button.click()

        # Open shopping cart from success popup
        cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'cart')))
        cart_button.click()

        # Accept terms of service and click "Checkout" button
        terms_of_service = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'terms-of-service'))))
        terms_of_service.click()
        checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='checkout']")))
        checkout_button.click()

        # Choose "Checkout as Guest"
        checkout_as_guest_radio = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'guest')))
        checkout_as_guest_radio.click()

        # Fill in billing address
        first_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'FirstName')))
        first_name_input.send_keys('Test')
        last_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'LastName')))
        last_name_input.send_keys('User')
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'Email')))
        email_input.send_keys('random_email')
        city_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'City')))
        city_input.send_keys('Riga')
        address1_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'Address1')))
        address1_input.send_keys('Street 1')
        zip_postal_code_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'ZipPostalCode')))
        zip_postal_code_input.send_keys('LV-1234')

        # Select shipping and payment methods
        shipping_option_radio = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='shippingoption_1']")))
        shipping_option_radio.click()
        payment_method_radio = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='paymentmethod_1']")))
        payment_method_radio.click()

        # Enter credit card details
        credit_card_type_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'CreditCardType')))
        credit_card_type_input.send_keys('visa')
        cardholder_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'CardHolderName')))
        cardholder_name_input.send_keys('Test User')
        card_number_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'CardNumber')))
        card_number_input.send_keys('4111111111111111')
        expire_month_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'ExpireMonth')))
        expire_month_input.send_keys('4')
        expire_year_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'ExpireYear')))
        expire_year_input.send_keys('2027')
        card_code_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'CardCode')))
        card_code_input.send_keys('123')

        # Confirm the order
        confirm_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='confirm']")))
        confirm_button.click()

        # Validate that the confirmation message or success section is visible
        order_completion_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='order-completion-message']")))
        self.assertEqual(order_completion_message.text, 'Thank you for your order!')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()