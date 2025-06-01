from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Search for a product
        search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        search_button.click()

        # Add a product to the cart
        add_to_cart_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Go to cart from popup
        cart_popup_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification")))
        cart_link = cart_popup_button.find_element(By.CSS_SELECTOR, "a[href='/cart']")
        cart_link.click()

        # Click Checkout as Guest
        checkout_as_guest_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill billing form
        self.wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        
        # Continue to shipping method
        continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        self.wait.until(EC.element_to_be_clickable(continue_button)).click()

        # Select shipping method
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#shippingoption_1"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shipping-method-next-step-button"))).click()

        # Select payment method
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#paymentmethod_1"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-method-next-step-button"))).click()

        # Fill payment information
        self.wait.until(EC.visibility_of_element_located((By.ID, "CardholderName"))).send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        
        # Continue to confirm order
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-info-next-step-button"))).click()

        # Confirm order
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button"))).click()

        # Verify order completion
        order_completion_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Your order has been successfully processed!')]")))
        self.assertIsNotNone(order_completion_message, "Order completion message not found. Test failed!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()