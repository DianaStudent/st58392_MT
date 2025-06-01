import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait
        
        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Cookies accept button not found.")

        # Navigate to login page
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/login')]")))
            login_link.click()
        except:
            self.fail("Login link not found.")
        
        # Perform login
        try:
            email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_input = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']/..")

            email_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except:
            self.fail("Login elements not found or could not log in.")

        # Add products to cart
        try:
            product_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/following-sibling::div/button[@title='Add to cart']")))
            product_button.click()
            
            product_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/chair']/following-sibling::div/button[@title='Add to cart']")))
            product_button.click()
        except:
            self.fail("Product add buttons not found.")

        # Go to cart page
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
            cart_button.click()

            proceed_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/checkout')]")))
            proceed_to_checkout_button.click()
        except:
            self.fail("Failed to navigate to checkout.")

        # Fill in billing details
        try:
            first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
            last_name_input = driver.find_element(By.NAME, "lastName")
            address_input = driver.find_element(By.NAME, "address")
            city_input = driver.find_element(By.NAME, "city")
            postal_code_input = driver.find_element(By.NAME, "postalCode")
            phone_input = driver.find_element(By.NAME, "phone")
            email_input = driver.find_element(By.NAME, "email")

            first_name_input.send_keys("John")
            last_name_input.send_keys("Doe")
            address_input.send_keys("123 Elm Street")
            city_input.send_keys("Metropolis")
            postal_code_input.send_keys("12345")
            phone_input.send_keys("1234567890")
            email_input.send_keys("test22@user.com")
        except:
            self.fail("Billing form elements not found or could not be filled.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()