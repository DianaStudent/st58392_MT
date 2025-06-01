from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://example.com")  # Replace with the actual URL

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for a product
        try:
            search_box = wait.until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
            search_box.send_keys(Keys.RETURN)
        except:
            self.fail("Search box not found.")

        # Add the first product in the search results to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "(//button[contains(@class, 'product-box-add-to-cart-button')])[1]",
                    )
                )
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found in search results.")

        # Click "Shopping Cart" from the success popup
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
            )
            cart_button.click()
        except:
            self.fail("Shopping cart link in success popup not found.")

        # Agree with terms of service and proceed to checkout
        try:
            terms_checkbox = wait.until(
                EC.element_to_be_clickable((By.ID, "termsofservice"))
            )
            terms_checkbox.click()

            checkout_button = wait.until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )
            checkout_button.click()
        except:
            self.fail("Terms of service checkbox or checkout button not found.")

        # Use the Checkout as Guest option
        try:
            checkout_as_guest_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            checkout_as_guest_button.click()
        except:
            self.fail("Checkout as guest button not found.")

        # Fill billing form
        try:
            driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
            driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
            driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email@test.com")
            driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
            driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
            driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
            driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
            driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
            
            continue_button = wait.until(
                EC.element_to_be_clickable((By.NAME, "save"))
            )
            continue_button.click()
        except:
            self.fail("Billing form elements not found.")

        # Select shipping method
        try:
            shipping_option = wait.until(
                EC.element_to_be_clickable((By.ID, "shippingoption_1"))
            )
            shipping_option.click()

            shipping_continue_button = driver.find_element(
                By.CLASS_NAME, "shipping-method-next-step-button"
            )
            shipping_continue_button.click()
        except:
            self.fail("Shipping method elements not found.")

        # Select payment method
        try:
            payment_method_option = wait.until(
                EC.element_to_be_clickable((By.ID, "paymentmethod_1"))
            )
            payment_method_option.click()

            payment_continue_button = driver.find_element(
                By.CLASS_NAME, "payment-method-next-step-button"
            )
            payment_continue_button.click()
        except:
            self.fail("Payment method elements not found.")

        # Fill payment information
        try:
            driver.find_element(By.ID, "CardholderName").send_keys("Test User")
            driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
            driver.find_element(By.ID, "ExpireMonth").send_keys("04")
            driver.find_element(By.ID, "ExpireYear").send_keys("2027")
            driver.find_element(By.ID, "CardCode").send_keys("123")

            payment_info_continue_button = driver.find_element(
                By.CLASS_NAME, "payment-info-next-step-button"
            )
            payment_info_continue_button.click()
        except:
            self.fail("Payment information elements not found.")

        # Confirm order
        try:
            confirm_order_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button"))
            )
            confirm_order_button.click()
        except:
            self.fail("Confirm order button not found.")

        # Check for order completion message
        try:
            order_complete_message = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "order-completed-title"))
            )
            self.assertIn("Your order has been successfully processed!", order_complete_message.text)
        except:
            self.fail("Order completion message not found or incorrect.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()