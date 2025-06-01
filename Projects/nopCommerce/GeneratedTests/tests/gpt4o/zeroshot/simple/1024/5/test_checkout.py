import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Search for 'book'
        search_box = wait.until(EC.presence_of_element_located((By.ID, 'small-searchterms')))
        search_box.send_keys('book')
        search_box.submit()

        # Add the first product to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Go to cart from the success popup
        cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Checkout as Guest
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill billing form
        self.fill_billing_address_form()

        # Select Shipping method
        shipping_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#shippingoption_1")))
        shipping_option.click()

        continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shipping-method-next-step-button")))
        continue_button.click()

        # Select Payment method
        payment_method_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#paymentmethod_1")))
        payment_method_option.click()

        continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-method-next-step-button")))
        continue_button.click()

        # Fill Payment information
        self.fill_payment_information()

        # Confirm order
        confirm_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_order_button.click()

        # Verify order completion
        message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".order-completed .title"))
        )
        self.assertIn("Your order has been successfully processed!", message.text)

    def fill_billing_address_form(self):
        driver = self.driver
        wait = self.wait

        inputs = {
            'BillingNewAddress_FirstName': "Test",
            'BillingNewAddress_LastName': "User",
            'BillingNewAddress_Email': "random_email@test.com",
            'BillingNewAddress_CountryId': "124",
            'BillingNewAddress_City': "Riga",
            'BillingNewAddress_Address1': "Street 1",
            'BillingNewAddress_ZipPostalCode': "LV-1234",
            'BillingNewAddress_PhoneNumber': "12345678"
        }

        for field_id, value in inputs.items():
            field = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            field.clear()
            field.send_keys(value)

        continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".new-address-next-step-button")))
        continue_button.click()

    def fill_payment_information(self):
        driver = self.driver
        wait = self.wait

        inputs = {
            'CardholderName': "Test User",
            'CardNumber': "4111111111111111",
            'CardCode': "123",
        }

        for field_id, value in inputs.items():
            field = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            field.clear()
            field.send_keys(value)

        expiry_month = wait.until(EC.presence_of_element_located((By.ID, "ExpireMonth")))
        expiry_month.send_keys("4")
        
        expiry_year = wait.until(EC.presence_of_element_located((By.ID, "ExpireYear")))
        expiry_year.send_keys("2027")

        continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-info-next-step-button")))
        continue_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()