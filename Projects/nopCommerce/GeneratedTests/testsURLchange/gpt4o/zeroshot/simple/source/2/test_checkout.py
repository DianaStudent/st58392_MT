from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class CheckoutTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
    
    def test_checkout_process(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 20)

            # Search for a product
            search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
            search_box.send_keys("book")
            search_button = driver.find_element(By.CSS_SELECTOR, "#small-search-box-form > button")
            search_button.click()

            # Add to cart
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")))
            add_to_cart_button.click()

            # Go to cart from success popup
            go_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.bar-notification.success a")))
            go_to_cart_button.click()

            # Checkout as guest
            checkout_button = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
            checkout_button.click()
            checkout_as_guest_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.checkout-as-guest-button")))
            checkout_as_guest_button.click()

            # Fill billing information
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
            driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
            driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
            driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
            driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
            driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
            driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
            country_dropdown = driver.find_element(By.ID, "BillingNewAddress_CountryId")
            country_dropdown.send_keys("Latvia")
            state_dropdown = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
            state_dropdown.send_keys("Other")
            driver.find_element(By.CSS_SELECTOR, "button.new-address-next-step-button").click()
            
            # Select shipping method
            shipping_option = wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
            shipping_option.click()
            driver.find_element(By.CSS_SELECTOR, "button.shipping-method-next-step-button").click()

            # Select payment method
            payment_method_option = wait.until(EC.element_to_be_clickable((By.ID, "paymentmethod_1")))
            payment_method_option.click()
            driver.find_element(By.CSS_SELECTOR, "button.payment-method-next-step-button").click()

            # Enter payment information
            driver.find_element(By.ID, "CardholderName").send_keys("Test User")
            driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
            driver.find_element(By.ID, "ExpireMonth").send_keys("04")
            driver.find_element(By.ID, "ExpireYear").send_keys("2027")
            driver.find_element(By.ID, "CardCode").send_keys("123")
            driver.find_element(By.CSS_SELECTOR, "button.payment-info-next-step-button").click()

            # Confirm order
            confirm_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.confirm-order-next-step-button")))
            confirm_order_button.click()

            # Verify order completion
            thank_you_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.section.order-completed h1")))
            self.assertTrue("Thank you" in thank_you_message.text)

        except Exception as e:
            self.fail(f"Test failed due to an error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()