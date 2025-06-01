from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        
        # Close the cookie consent
        self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))).click()

        # Click on Login
        account_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 
                          "button.account-setting-active")))
        account_button.click()
        login_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()

        # Log in
        username = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password = driver.find_element(By.NAME, "loginPassword")
        login_button = driver.find_element(By.XPATH, "//button//span[contains(text(), 'Login')]")
        username.send_keys("test22@user.com")
        password.send_keys("test**11")
        login_button.click()

        # Add product to cart
        add_to_cart_buttons = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//button[@title='Add to cart']")))
        if not add_to_cart_buttons:
            self.fail("No Add to Cart buttons found.")
        add_to_cart_buttons[0].click()
        
        # Open the cart
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
                               ".icon-cart")))
        cart_button.click()

        # Proceed to checkout
        proceed_to_checkout_button = self.wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # Fill in the billing form
        first_name = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        last_name = driver.find_element(By.NAME, "lastName")
        address = driver.find_element(By.NAME, "address")
        city = driver.find_element(By.NAME, "city")
        postal_code = driver.find_element(By.NAME, "postalCode")
        phone = driver.find_element(By.NAME, "phone")
        email = driver.find_element(By.NAME, "email")

        first_name.send_keys("John")
        last_name.send_keys("Doe")
        address.send_keys("1234 Test St")
        city.send_keys("Testville")
        postal_code.send_keys("12345")
        phone.send_keys("1234567890")
        email.send_keys("test22@user.com")

        # Wait for state select field to be visible and enter value
        state_select = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//select[@name='state']")))
        state_select.click()
        state_option = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//select[@name='state']/option[@value='QC']")))
        state_option.click()

        # Accept terms and place order
        accept_terms = driver.find_element(By.NAME, "isAgree")
        accept_terms.click()
        place_order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Place your order')]")
        if not place_order_button:
            self.fail("Place Order button not found.")
        place_order_button.click()

        # Verify order placement
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, 
                "//div[contains(text(), 'Thank you for your order')]")))
        except:
            self.fail("Order confirmation not found.")
          
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()