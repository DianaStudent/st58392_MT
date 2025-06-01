from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        # Open the homepage.
        self.driver.get("http://localhost:8080/en/")
        
        # Click the login link from the top navigation.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-name='Login']"))
        ).click()
        
        # Wait for the login page to load.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        
        # Fill in the email and password fields using test credentials provided.
        self.driver.find_element(By.ID, "email").send_keys("test@user.com")
        self.driver.find_element(By.ID, "password").send_keys("test@user1")
        
        # Click the submit button.
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-name='Submit']"))
        ).click()
        
        # Wait for the redirect after login.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-name='Sign out']"))
        )
        
        # Confirm that login was successful by checking that:
        self.assertTrue(EC.presence_of_element_located((By.XPATH, "//a[@data-name='Sign out']")))
        self.driver.find_element(By.ID, "username").get_attribute("innerHTML") != ""
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()