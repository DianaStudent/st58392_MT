import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        
        # Step 2: Search for a product
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()
        
        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        
        search_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-button")))
        search_button.click()
        
        # Step 3: Add to cart the first item in the search results
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()
        
        # Step 4: Open the shopping cart via the success notification popup
        cart_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        cart_link.click()
        
        # Step 5: Accept terms of service and Checkout
        terms_checkbox = self.wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        
        checkout_button = self.wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        checkout_button.click()
        
        # Step 6: Choose "Checkout as Guest"
        checkout_as_guest_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()
        
        # Step 7: Fill in the billing address
        self.fill_billing_address()

        # Step 8: Select shipping and payment methods
        self.choose_shipping_method()
        self.choose_payment_method()

        # Step 9: Enter credit card details
        self.enter_payment_information()

        # Step 10: Confirm the order
        confirm_order_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confirm-order-next-step-button")))
        confirm_order_button.click()

        # Step 11: Validate order confirmation
        success_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "order-completed")))
        self.assertTrue(success_message.is_displayed())

    def fill_billing_address(self):
        inputs = {
            "BillingNewAddress_FirstName": "Test",
            "BillingNewAddress_LastName": "User",
            "BillingNewAddress_Email": "random_email",
            "BillingNewAddress_City": "Riga",
            "BillingNewAddress_Address1": "Street 1",
            "BillingNewAddress_ZipPostalCode": "LV-1234",
            "BillingNewAddress_PhoneNumber": "12345678",
        }
        
        for field_id, value in inputs.items():
            input_element = self.wait.until(EC.presence_of_element_located((By.ID, field_id)))
            input_element.clear()
            input_element.send_keys(value)
        
        country_select = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
        country_select.send_keys("Latvia")
        
        continue_button = self.wait.until(EC.presence_of_element_located((By.NAME, "save")))
        continue_button.click()

    def choose_shipping_method(self):
        shipping_option = self.wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1")))
        shipping_option.click()
        
        continue_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shipping-method-next-step-button")))
        continue_button.click()

    def choose_payment_method(self):
        payment_option = self.wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_option.click()
        
        continue_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "payment-method-next-step-button")))
        continue_button.click()

    def enter_payment_information(self):
        inputs = {
            "CardholderName": "Test User",
            "CardNumber": "4111111111111111",
            "ExpireMonth": "04",
            "ExpireYear": "2027",
            "CardCode": "123",
        }
        
        for field_id, value in inputs.items():
            input_element = self.wait.until(EC.presence_of_element_located((By.ID, field_id)))
            input_element.clear()
            input_element.send_keys(value)
        
        continue_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "payment-info-next-step-button")))
        continue_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()