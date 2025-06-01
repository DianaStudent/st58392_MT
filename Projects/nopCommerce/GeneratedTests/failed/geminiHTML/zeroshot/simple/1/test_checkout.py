from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for a product
        try:
            search_box = wait.until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
            search_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search failed: {e}")

        # Add the first product to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart failed: {e}")

        # Go to shopping cart
        try:
            shopping_cart_link = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']"))
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to shopping cart: {e}")

        # Checkout
        try:
            checkout_button = wait.until(
                EC.presence_of_element_located((By.ID, "checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Checkout button not found: {e}")

        # Checkout as guest
        try:
            guest_checkout_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            guest_checkout_button.click()
        except Exception as e:
            self.fail(f"Guest checkout button not found: {e}")

        # Billing form
        try:
            first_name = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
            )
            first_name.send_keys("Test")

            last_name = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))
            )
            last_name.send_keys("User")

            email = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))
            )
            email.send_keys("random_email")

            country = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
            )
            country.send_keys("Latvia")

            state = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))
            )
            state.send_keys("Other")

            city = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))
            )
            city.send_keys("Riga")

            address1 = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))
            )
            address1.send_keys("Street 1")

            zip_code = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))
            )
            zip_code.send_keys("LV-1234")

            phone_number = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))
            )
            phone_number.send_keys("12345678")

            billing_continue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
            )
            billing_continue_button.click()

        except Exception as e:
            self.fail(f"Billing form filling failed: {e}")

        # Shipping method
        try:
            shipping_method = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#shippingoption_1"))
            )
            shipping_method.click()

            shipping_continue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
            )
            shipping_continue_button.click()
        except Exception as e:
            self.fail(f"Shipping method selection failed: {e}")

        # Payment method
        try:
            payment_method = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#paymentmethod_1"))
            )
            payment_method.click()

            payment_continue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
            )
            payment_continue_button.click()
        except Exception as e:
            self.fail(f"Payment method selection failed: {e}")

        # Payment information
        try:
            card_type = wait.until(
                EC.presence_of_element_located((By.ID, "CreditCardType"))
            )
            card_type.send_keys("visa")

            cardholder_name = wait.until(
                EC.presence_of_element_located((By.ID, "CardholderName"))
            )
            cardholder_name.send_keys("Test User")

            card_number = wait.until(
                EC.presence_of_element_located((By.ID, "CardNumber"))
            )
            card_number.send_keys("4111111111111111")

            expire_month = wait.until(
                EC.presence_of_element_located((By.ID, "ExpireMonth"))
            )
            expire_month.send_keys("4")

            expire_year = wait.until(
                EC.presence_of_element_located((By.ID, "ExpireYear"))
            )
            expire_year.send_keys("2027")

            card_code = wait.until(
                EC.presence_of_element_located((By.ID, "CardCode"))
            )
            card_code.send_keys("123")

            payment_info_continue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "payment-info-next-step-button"))
            )
            payment_info_continue_button.click()
        except Exception as e:
            self.fail(f"Payment information filling failed: {e}")

        # Confirm order
        try:
            confirm_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button"))
            )
            confirm_button.click()
        except Exception as e:
            self.fail(f"Confirm order button not found: {e}")

        # Verify order completion
        try:
            order_completed_message = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='title']/strong[text()='Your order has been successfully processed!']"))
            )
            self.assertTrue(order_completed_message.is_displayed())
        except Exception as e:
            self.fail(f"Order completion message not found: {e}")


if __name__ == "__main__":
    unittest.main()