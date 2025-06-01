from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))

    def test_login(self):
        sign_in_button = self.driver.find_element(By.LINK_TEXT, "Sign in")
        sign_in_button.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
        
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        
        email_input.send_keys("test@user.com")
        password_input.send_keys("test@user1")

        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign out")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()