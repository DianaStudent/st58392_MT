import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestCheckoutProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")

    def test_checkout_process(self):
        # Find search link and click it
        search_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        # Search for a product (e.g. "book")
        search_input = self.driver.find_element(By.NAME, "search_query")
        search_input.send_keys("book")

        # Click the submit button
        search_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "submit_search")))
        search_button.click()

        # Find and add first item to cart
        add_to_cart_button = self.driver.find_element(By.XPATH, "//div[@class='product']/form/button")
        add_to_cart_button.click()

        # Open shopping cart via success notification popup
        view_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Accept terms of service and click the "Checkout" button
        accept_terms_checkbox = self.driver.find_element(By.ID, "terms_of_service")
        accept_terms_checkbox.click()
        checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
        checkout_button.click()

        # Choose "Checkout as Guest"
        guest_checkout_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout as Guest")))
        guest_checkout_link.click()

        # Fill in billing address
        self.fill_billing_address()

        # Select shipping and payment methods
        self.select_shipping_method()
        self.select_payment_method()

        # Enter credit card details
        self.enter_credit_card_details()

        # Confirm the order
        confirm_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Confirm Order")))
        confirm_button.click()

        # Validate that the confirmation message or success section is visible
        self.validate_order_completion()

    def fill_billing_address(self):
        first_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "firstName")))
        last_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "lastName")))
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "email")))
        city_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "city")))
        address1_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "address1")))
        zip_postal_code_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "zipPostalCode")))
        phone_number_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "phoneNumber")))

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys("random_email")
        city_input.send_keys("Riga")
        address1_input.send_keys("Street 1")
        zip_postal_code_input.send_keys("LV-1234")
        phone_number_input.send_keys("12345678")

    def select_shipping_method(self):
        shipping_option = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
        shipping_option.click()

    def select_payment_method(self):
        payment_method_option = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "paymentmethod_1")))
        payment_method_option.click()

    def enter_credit_card_details(self):
        cardholder_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "cardHolderName")))
        card_number_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "cardNumber")))
        expire_month_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "expireMonth")))
        expire_year_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "expireYear")))
        card_code_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "cardCode")))

        cardholder_name_input.send_keys("Test User")
        card_number_input.send_keys("4111111111111111")
        expire_month_input.send_keys("12")
        expire_year_input.send_keys("2025")
        card_code_input.send_keys("123")

    def validate_order_completion(self):
        success_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='success']")))
        self.assertTrue(success_message.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()