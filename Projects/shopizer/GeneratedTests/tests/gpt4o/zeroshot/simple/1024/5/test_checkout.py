import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
    
    def test_checkout_process(self):
        driver = self.driver
        
        # Accept cookies
        try:
            accept_cookies_btn = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_btn.click()
        except:
            self.fail("Accept cookies button not found")
        
        # Go to login page
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active"))
            )
            account_button.click()
            
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("Login elements not found")
        
        # Perform Login
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            
            email_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except:
            self.fail("Login form elements not found")
        
        # Add first product to cart
        try:
            add_to_cart_btn = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']"))
            )
            add_to_cart_btn.click()
        except:
            self.fail("Add to cart button not found")
        
        # Open cart and proceed to checkout
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.icon-cart"))
            )
            cart_button.click()
            
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))
            )
            checkout_button.click()
        except:
            self.fail("Cart or checkout elements not found")
        
        # Fill in Billing Information
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            last_name_input = driver.find_element(By.NAME, "lastName")
            address_input = driver.find_element(By.NAME, "address")
            city_input = driver.find_element(By.NAME, "city")
            postal_code_input = driver.find_element(By.NAME, "postalCode")
            phone_input = driver.find_element(By.NAME, "phone")
            email_input = driver.find_element(By.NAME, "email")
            place_order_btn = driver.find_element(By.CSS_SELECTOR, "button[type='button']")
            
            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            address_input.send_keys("123 Street")
            city_input.send_keys("City")
            postal_code_input.send_keys("H2H-2H2")
            phone_input.send_keys("8888888888")
            email_input.send_keys("test22@user.com")
            
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "isAgree"))
            ).click()
            
            place_order_btn.click()
            
        except:
            self.fail("Billing form elements not found or interaction failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()