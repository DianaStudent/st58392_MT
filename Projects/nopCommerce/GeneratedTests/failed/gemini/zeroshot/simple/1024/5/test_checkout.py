from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for a product
        try:
            search_input = wait.until(EC.element_to_be_clickable((By.ID, "small-searchterms")))
            search_input.send_keys("book")
            search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button")))
            search_button.click()
        except Exception as e:
            self.fail(f"Search failed: {e}")

        # Add the first product to the cart
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Adding to cart failed: {e}")
            
        # Go to the shopping cart
        try:
            shopping_cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='bar-notification']//a[contains(@href, '/cart')]")))
            shopping_cart_link.click()
        except:
            try:
                go_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mini-shopping-cart']//button[contains(text(), 'Go to cart')]")))
                go_to_cart_button.click()
            except Exception as e:
                self.fail(f"Failed to navigate to shopping cart: {e}")

        # Checkout
        try:
            terms_of_service = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
            terms_of_service.click()
            checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
            checkout_button.click()
        except Exception as e:
            self.fail(f"Checkout initiation failed: {e}")

        # Checkout as guest
        try:
            checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
            checkout_as_guest_button.click()
        except Exception as e:
            self.fail(f"Checkout as guest failed: {e}")

        # Billing form
        try:
            first_name_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_FirstName")))
            first_name_input.send_keys("Test")
            last_name_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_LastName")))
            last_name_input.send_keys("User")
            email_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_Email")))
            email_input.send_keys("random_email")
            country_select = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
            country_select.send_keys("Latvia")
            state_select = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId")))
            state_select.send_keys("Other")
            city_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_City")))
            city_input.send_keys("Riga")
            address1_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_Address1")))
            address1_input.send_keys("Street 1")
            zip_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_ZipPostalCode")))
            zip_input.send_keys("LV-1234")
            phone_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_PhoneNumber")))
            phone_input.send_keys("12345678")
            billing_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button")))
            billing_continue_button.click()
        except Exception as e:
            self.fail(f"Billing form failed: {e}")

        # Shipping method
        try:
            shipping_option = wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
            shipping_option.click()
            shipping_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button")))
            shipping_continue_button.click()
        except Exception as e:
            self.fail(f"Shipping method failed: {e}")

        # Payment method
        try:
            payment_method_option = wait.until(EC.element_to_be_clickable((By.ID, "paymentmethod_1")))
            payment_method_option.click()
            payment_method_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button")))
            payment_method_continue_button.click()
        except Exception as e:
            self.fail(f"Payment method failed: {e}")

       # Payment information
        try:
            credit_card_type = wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
            credit_card_type.send_keys("visa")
            cardholder_name = wait.until(EC.presence_of_element_located((By.ID, "CardholderName")))
            cardholder_name.send_keys("Test User")
            card_number = wait.until(EC.presence_of_element_located((By.ID, "CardNumber")))
            card_number.send_keys("4111111111111111")
            expire_month = wait.until(EC.presence_of_element_located((By.ID, "ExpireMonth")))
            expire_month.send_keys("4")
            expire_year = wait.until(EC.presence_of_element_located((By.ID, "ExpireYear")))
            expire_year.send_keys("2027")
            card_code = wait.until(EC.presence_of_element_located((By.ID, "CardCode")))
            card_code.send_keys("123")
            payment_info_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment-info-next-step-button")))
            payment_info_continue_button.click()
        except Exception as e:
            self.fail(f"Payment information failed: {e}")

        # Confirm order
        try:
            confirm_order_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button")))
            confirm_order_button.click()
        except Exception as e:
            self.fail(f"Confirm order failed: {e}")

        # Verify order completion
        try:
            order_completed_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='title']/strong[contains(text(), 'Your order has been successfully processed!')]")))
            self.assertIn("Your order has been successfully processed!", order_completed_message.text)
        except Exception as e:
            self.fail(f"Order completion verification failed: {e}")

if __name__ == "__main__":
    unittest.main()