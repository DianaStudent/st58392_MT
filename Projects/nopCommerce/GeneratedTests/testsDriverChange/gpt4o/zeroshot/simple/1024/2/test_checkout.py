import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Search for "book"
        search_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_field.send_keys("book")
        search_field.send_keys(Keys.RETURN)

        # Add the first product to the cart
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Click "shopping cart" in the success notification
        go_to_cart_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p.content a[href='/cart']"))
        )
        go_to_cart_link.click()

        # Proceed to checkout as guest
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
        )
        checkout_button.click()

        checkout_as_guest_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # Fill billing information
        self.fill_billing_information()

        # Continue to shipping method
        continue_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing-buttons-container .new-address-next-step-button"))
        )
        continue_button.click()

        # Select shipping option
        shipping_option = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#shippingoption_1"))
        )
        shipping_option.click()
        continue_button = driver.find_element(By.CSS_SELECTOR, "#shipping-method-buttons-container .shipping-method-next-step-button")
        continue_button.click()

        # Select payment method
        payment_method_option = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#paymentmethod_1"))
        )
        payment_method_option.click()
        continue_button = driver.find_element(By.CSS_SELECTOR, "#payment-method-buttons-container .payment-method-next-step-button")
        continue_button.click()

        # Fill payment information
        self.fill_payment_information()

        # Confirm order
        confirm_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#confirm-order-buttons-container .confirm-order-next-step-button"))
        )
        confirm_button.click()

        # Verify order completion
        try:
            order_complete_message = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(., 'Your order has been successfully processed!')]"))
            )
        except:
            self.fail("Order completion message not found.")

    def fill_billing_information(self):
        driver = self.driver
        fields = {
            "BillingNewAddress_FirstName": "Test",
            "BillingNewAddress_LastName": "User",
            "BillingNewAddress_Email": "random_email",
            "BillingNewAddress_City": "Riga",
            "BillingNewAddress_Address1": "Street 1",
            "BillingNewAddress_ZipPostalCode": "LV-1234",
            "BillingNewAddress_PhoneNumber": "12345678"
        }

        for field_id, value in fields.items():
            field = self.wait.until(
                EC.presence_of_element_located((By.ID, field_id))
            )
            field.clear()
            field.send_keys(value)

        country_dropdown = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        country_dropdown.send_keys(Keys.DOWN * 124)  # Assuming United States (ID: 124)

    def fill_payment_information(self):
        driver = self.driver
        payment_fields = {
            "CardholderName": "Test User",
            "CardNumber": "4111111111111111",
            "ExpireMonth": "4",
            "ExpireYear": "2027",
            "CardCode": "123"
        }

        for field_id, value in payment_fields.items():
            field = self.wait.until(
                EC.presence_of_element_located((By.ID, field_id))
            )
            field.clear()
            field.send_keys(value)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()