import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        
        try:
            # Header Links
            header_links = driver.find_element(By.CLASS_NAME, "header-links")
            self.assertTrue(header_links.is_displayed())
            
            # Register Link
            register_link = driver.find_element(By.LINK_TEXT, "Register")
            self.assertTrue(register_link.is_displayed())

            # Log in Link
            login_link = driver.find_element(By.LINK_TEXT, "Log in")
            self.assertTrue(login_link.is_displayed())

            # Main Page Title
            page_title = driver.find_element(By.CLASS_NAME, "page-title")
            self.assertTrue(page_title.is_displayed())

            # Form Elements
            gender_male = driver.find_element(By.ID, "gender-male")
            self.assertTrue(gender_male.is_displayed())

            gender_female = driver.find_element(By.ID, "gender-female")
            self.assertTrue(gender_female.is_displayed())

            first_name = driver.find_element(By.ID, "FirstName")
            self.assertTrue(first_name.is_displayed())

            last_name = driver.find_element(By.ID, "LastName")
            self.assertTrue(last_name.is_displayed())

            email = driver.find_element(By.ID, "Email")
            self.assertTrue(email.is_displayed())

            password = driver.find_element(By.ID, "Password")
            self.assertTrue(password.is_displayed())

            confirm_password = driver.find_element(By.ID, "ConfirmPassword")
            self.assertTrue(confirm_password.is_displayed())

            # Register Button
            register_button = driver.find_element(By.ID, "register-button")
            self.assertTrue(register_button.is_displayed())
        
        except Exception as e:
            self.fail(f"An element is missing or not visible: {e}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()