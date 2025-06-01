from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Search for a product
            search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
            search_box.send_keys("book", Keys.RETURN)

            # Add to cart
            add_to_cart_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.product-box-add-to-cart-button")
            ))
            add_to_cart_button.click()

            # Click on "shopping cart" from the success popup
            go_to_cart = wait.until(EC.presence_of_element_located(
                (By.LINK_TEXT, "shopping cart")
            ))
            go_to_cart.click()

            # Checkout as guest
            checkout_as_guest_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.checkout-as-guest-button")
            ))
            checkout_as_guest_button.click()

            # Fill billing info
            driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
            driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
            driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
            driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
            driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
            driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
            driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
            driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

            # Continue to shipping
            billing_continue_button = driver.find_element(By.CSS_SELECTOR, "button.new-address-next-step-button")
            billing_continue_button.click()

            # Choose shipping option
            shipping_option = wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
            shipping_option.click()
            shipping_continue_button = driver.find_element(By.CSS_SELECTOR, "button.shipping-method-next-step-button")
            shipping_continue_button.click()

            # Choose payment method
            payment_method = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
            payment_method.click()
            payment_continue_button = driver.find_element(By.CSS_SELECTOR, "button.payment-method-next-step-button")
            payment_continue_button.click()

            # Fill payment information
            driver.find_element(By.ID, "CreditCardType").send_keys("visa")
            driver.find_element(By.ID, "CardholderName").send_keys("Test User")
            driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
            driver.find_element(By.ID, "ExpireMonth").send_keys("04")
            driver.find_element(By.ID, "ExpireYear").send_keys("2027")
            driver.find_element(By.ID, "CardCode").send_keys("123")

            # Continue to confirm order
            payment_info_continue_button = driver.find_element(By.CSS_SELECTOR, "button.payment-info-next-step-button")
            payment_info_continue_button.click()

            # Confirm order
            confirm_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.confirm-order-next-step-button")))
            confirm_order_button.click()

            # Check for order completion
            thank_you_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.order-completed strong")))
            self.assertEqual(thank_you_message.text, "Your order has been successfully processed!")

        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()