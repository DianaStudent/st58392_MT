import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestOrderFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://example.com") # replace with actual URL

    def test_order_flow(self):
        search_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "search_query")))
        search_input.send_keys("book")
        search_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "submit")))
        search_button.click()

        # Add first item to cart
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-add-to-cart-button")))
        add_to_cart_button.click()

        # Open shopping cart
        success_popup = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "success-notification")))
        cart_button = WebDriverWait(success_popup, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Shopping Cart")))
        cart_button.click()

        # Proceed to checkout
        terms_of_service_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "terms-of-service")))
        terms_of_service_checkbox.click()
        checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
        checkout_button.click()

        # Checkout as guest
        guest_checkout_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout as Guest")))
        guest_checkout_link.click()

        # Fill in billing address
        first_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "BillingAddress_FirstName")))
        last_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "BillingAddress_LastName")))
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "BillingAddress_Email")))
        city_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "BillingAddress_City")))
        address1_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "BillingAddress_Address1")))
        zip_postal_code_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "BillingAddress_ZipPostalCode")))
        phone_number_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "BillingAddress_PhoneNumber")))

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys("random_email")
        city_input.send_keys("Riga")
        address1_input.send_keys("Street 1")
        zip_postal_code_input.send_keys("LV-1234")
        phone_number_input.send_keys("12345678")

        # Select shipping and payment methods
        select_shipping_method_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "select-shipping-method")))
        select_shipping_method_button.click()
        select_payment_method_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "select-payment-method")))
        select_payment_method_button.click()

        # Enter credit card details
        credit_card_type_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "CreditCardType")))
        credit_card_type_select.send_keys("visa")
        cardholder_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "CardHolderName")))
        card_number_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "CardNumber")))
        expire_month_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "ExpireMonth")))
        expire_year_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "ExpireYear")))
        card_code_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "CardCode")))

        cardholder_name_input.send_keys("Test User")
        card_number_input.send_keys("4111111111111111")
        expire_month_input.send_keys("4")
        expire_year_input.send_keys("2027")
        card_code_input.send_keys("123")

        # Proceed to payment
        proceed_to_payment_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Payment")))
        proceed_to_payment_button.click()

        # Verify order summary
        order_summary = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "order-summary")))
        self.assertTrue(order_summary.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()