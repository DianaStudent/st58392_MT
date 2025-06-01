import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to home page
        driver.get("http://localhost:8080")
        
        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception:
            self.fail("Accept cookies button not found or not clickable.")

        # Navigate to login page
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except Exception:
            self.fail("Login link not found or not clickable.")

        # Perform login
        try:
            email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            email_input.send_keys("test22@user.com")
            password_input = driver.find_element(By.NAME, "loginPassword")
            password_input.send_keys("test**11")
            login_button = driver.find_element(By.XPATH, "//button[span[text()='Login']]")
            login_button.click()
        except Exception:
            self.fail("Failed to perform login.")

        # Add product 'Olive Table' to cart
        try:
            olive_table_add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3/a[text()='Olive Table']/following::button[@title='Add to cart']")))
            olive_table_add_to_cart_button.click()
        except Exception:
            self.fail("Cannot add Olive Table to cart.")

        # Navigate to Cart page
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
            cart_button.click()
        except Exception:
            self.fail("Cart button not found or not clickable.")

        # Proceed to Checkout
        try:
            proceed_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
            proceed_to_checkout_button.click()
        except Exception:
            self.fail("Proceed to Checkout button not found or not clickable.")

        # Fill in Billing form
        try:
            first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
            first_name_input.send_keys("Test")
            last_name_input = driver.find_element(By.NAME, "lastName")
            last_name_input.send_keys("User")
            address_input = driver.find_element(By.NAME, "address")
            address_input.send_keys("1234 Street address")
            city_input = driver.find_element(By.NAME, "city")
            city_input.send_keys("My city")
            postal_code_input = driver.find_element(By.NAME, "postalCode")
            postal_code_input.send_keys("H2H-2H2")
            phone_input = driver.find_element(By.NAME, "phone")
            phone_input.send_keys("8888888888")
            email_input = driver.find_element(By.NAME, "email")
            email_input.clear()
            email_input.send_keys("test22@user.com")
        except Exception:
            self.fail("Failed to fill in billing form.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()