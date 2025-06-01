from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')  # Replace with the correct URL of the home page
        self.driver.maximize_window()
    
    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Accept cookies
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail("Failed at cookies acceptance: " + str(e))
        
        # Navigate to login page
        try:
            login_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except Exception as e:
            self.fail("Failed to navigate to login page: " + str(e))
        
        # Login
        try:
            username_field = wait.until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            password_field = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
            
            username_field.send_keys("test22@user.com")
            password_field.send_keys("test**11")
            login_button.click()
        except Exception as e:
            self.fail("Login failed: " + str(e))
        
        # Add products to cart
        try:
            add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[contains(@title, 'Add to cart')]")
            for button in add_to_cart_buttons[:2]:  # Add first two products to the cart
                button.click()
        except Exception as e:
            self.fail("Failed to add products to cart: " + str(e))
        
        # Go to cart page
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart span.count-style"))
            )
            cart_button.click()
        except Exception as e:
            self.fail("Failed to open cart page: " + str(e))
        
        # Proceed to checkout
        try:
            proceed_to_checkout = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Proceed to Checkout']"))
            )
            proceed_to_checkout.click()
        except Exception as e:
            self.fail("Failed to proceed to checkout: " + str(e))
        
        # Fill in billing form
        try:
            first_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            last_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
            street_address_field = wait.until(EC.visibility_of_element_located((By.NAME, "address")))
            city_field = wait.until(EC.visibility_of_element_located((By.NAME, "city")))
            postal_code_field = wait.until(EC.visibility_of_element_located((By.NAME, "postalCode")))
            email_field_checkout = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            
            first_name_field.send_keys("Test")
            last_name_field.send_keys("User")
            street_address_field.send_keys("1234 Test St")
            city_field.send_keys("TestCity")
            postal_code_field.send_keys("H2H-2H2")
            email_field_checkout.send_keys("test22@user.com")
            
        except Exception as e:
            self.fail("Failed to fill billing form: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()