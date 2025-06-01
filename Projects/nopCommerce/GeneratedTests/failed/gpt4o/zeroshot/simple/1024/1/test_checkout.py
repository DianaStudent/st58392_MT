from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


class CheckoutProcessTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get('http://max/')

    def test_checkout_process(self):
        driver = self.driver

        # Search for a product
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
            search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-box-button")
            search_button.click()
        except:
            self.fail("Search elements not found or interaction failed.")

        # Add a product to cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".item-box .product-box-add-to-cart-button")
                )
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart elements not found or interaction failed.")

        # Go to cart from success popup
        try:
            go_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#bar-notification .cart-button")
                )
            )
            go_to_cart_button.click()
        except:
            self.fail("Go to cart button not found or interaction failed.")

        # Checkout as guest
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.checkout-as-guest-button")
                )
            ).click()
        except:
            self.fail("Checkout as guest button not found or interaction failed.")

        # Fill billing form
        try:
            driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
            driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
            driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
            driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("124")  # Latvia
            driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
            driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
            driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
            driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

            continue_button = driver.find_element(By.CSS_SELECTOR, "button.new-address-next-step-button")
            continue_button.click()
        except:
            self.fail("Billing form elements not found or interaction failed.")

        # Select shipping method
        try:
            shipping_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#shippingoption_1"))
            )
            shipping_option.click()
            continue_shipping_button = driver.find_element(
                By.CSS_SELECTOR, "button.shipping-method-next-step-button"
            )
            continue_shipping_button.click()
        except:
            self.fail("Shipping method selection failed or elements not found.")

        # Select payment method
        try:
            payment_method_option = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#paymentmethod_1"))
            )
            payment_method_option.click()
            continue_payment_button = driver.find_element(
                By.CSS_SELECTOR, "button.payment-method-next-step-button"
            )
            continue_payment_button.click()
        except:
            self.fail("Payment method selection failed or elements not found.")

        # Fill in payment information
        try:
            driver.find_element(By.ID, "CardholderName").send_keys("Test User")
            driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
            driver.find_element(By.ID, "ExpireMonth").send_keys("4")
            driver.find_element(By.ID, "ExpireYear").send_keys("2027")
            driver.find_element(By.ID, "CardCode").send_keys("123")
            continue_payment_info_button = driver.find_element(
                By.CSS_SELECTOR, "button.payment-info-next-step-button"
            )
            continue_payment_info_button.click()
        except:
            self.fail("Payment information elements not found or interaction failed.")

        # Confirm order
        try:
            confirm_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "button.confirm-order-next-step-button")
                )
            )
            confirm_button.click()
        except:
            self.fail("Confirm order elements not found or interaction failed.")

        # Verify order is completed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "order-completed"))
            )
        except:
            self.fail("Order completion message not found.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()