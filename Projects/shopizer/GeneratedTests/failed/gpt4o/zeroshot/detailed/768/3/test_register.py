from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
    
    def test_register_user(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Open home page
        driver.get("http://localhost/")
        
        # Accept cookies if needed
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except:
            pass  # If the accept button is not found, continue

        # Click on the account button
        account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
        account_button.click()
        
        # Select "Register" option
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()
        
        # Wait for the registration page to load
        wait.until(EC.url_contains("/register"))
        
        # Fill the registration form
        email = f"test_{int(time.time())}@user.com"
        form_data = {
            "email": email,
            "password": "test**11",
            "repeatPassword": "test**11",
            "firstName": "Test",
            "lastName": "User"
        }
        
        for key, value in form_data.items():
            element = wait.until(EC.presence_of_element_located((By.NAME, key)))
            element.clear()
            element.send_keys(value)

        # Select a country and state
        country_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[name='country']")))
        country_select.click()
        country_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[name='country'] option[value='CA']")))
        country_option.click()

        # Ensure dropdowns update and avoid overlay issues
        time.sleep(1)

        state_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[name='stateProvince']")))
        state_select.click()
        state_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[name='stateProvince'] option[value='QC']")))
        state_option.click()

        # Ensure dropdowns are deactivated
        time.sleep(1)

        # Submit the registration form
        register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Register')]")))
        register_button.click()
        
        # Wait for redirect and check success
        wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()