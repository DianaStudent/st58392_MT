from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAccessoriesPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
    
    def test_interface_elements(self):
        driver = self.driver
        
        # Check presence of key navigation links
        try:
            home_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']"))
            )
            clothes_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")
            accessories_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")
            art_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")
        except:
            self.fail("Navigation links are missing or not visible.")
        
        # Check presence of search input
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @name='s']"))
            )
        except:
            self.fail("Search input is missing or not visible.")
        
        # Check presence of button 'Sign in'
        try:
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']"))
            )
        except:
            self.fail("Sign in button is missing or not visible.")
        
        # Interact with an element - Click on 'Sign in' and verify navigation
        try:
            sign_in_button.click()
            WebDriverWait(driver, 20).until(
                EC.url_to_be("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
            )
        except:
            self.fail("Clicking 'Sign in' does not navigate to the login page.")
    
        # Verify the login page is displayed correctly
        try:
            login_email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
            )
            login_password_input = driver.find_element(By.XPATH, "//input[@type='password']")
            login_submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        except:
            self.fail("Login page elements are missing or not visible.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()