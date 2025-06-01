from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for a product
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book" + Keys.RETURN)

        # Add first product to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Go to shopping cart from success popup
        cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Checkout as Guest
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill Billing Information
        wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        
        country_dropdown = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        country_dropdown.send_keys(Keys.ENTER)
        country_dropdown.send_keys(Keys.DOWN)
        country_dropdown.send_keys(Keys.RETURN)
        
        # Continue to shipping method
        billing_continue_button = driver.find_element(By.NAME, "save")
        billing_continue_button.click()

        # Select Shipping Method
        shipping_method_radio = wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
        shipping_method_radio.click()
        shipping_continue_button = driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button")
        shipping_continue_button.click()

        # Select Payment Method
        payment_method_radio = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_method_radio.click()
        payment_method_continue_button = driver.find_element(By.NAME, "save")
        payment_method_continue_button.click()

        # Fill Payment Information
        wait.until(EC.element_to_be_clickable((By.ID, "CardholderName"))).send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        
        payment_info_continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button")
        payment_info_continue_button.click()

        # Confirm Order
        confirm_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_order_button.click()

        # Verify Order Completion
        success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "order-completed")))
        
        self.assertIn("Your order has been successfully processed!", success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()