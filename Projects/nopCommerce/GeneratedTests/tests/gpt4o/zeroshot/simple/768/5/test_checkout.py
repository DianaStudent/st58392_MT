import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Search for a product
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book")
        search_box.send_keys(Keys.RETURN)

        # Add the first product to the cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Go to shopping cart from success notification
        cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Proceed to checkout as guest
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        guest_checkout_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
        guest_checkout_button.click()

        # Fill out billing information
        self.fill_billing_information(driver)

        # Select shipping method
        next_step_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button")))
        next_step_button.click()

        # Select payment method
        payment_method = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#paymentmethod_1")))
        payment_method.click()
        next_step_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button")))
        next_step_button.click()

        # Fill out payment information
        self.fill_payment_information(driver)

        # Confirm order
        confirm_order_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button"))
        )
        confirm_order_button.click()

        # Verify order completion
        order_completed_text = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".order-completed .title strong")
        ))
        self.assertIn("Your order has been successfully processed!", order_completed_text.text)

    def fill_billing_information(self, driver):
        wait = self.wait
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        continue_button = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "new-address-next-step-button")))
        continue_button.click()

    def fill_payment_information(self, driver):
        wait = self.wait
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        continue_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "payment-info-next-step-button"))
        )
        continue_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()