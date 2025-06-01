from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        # Login
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/login']"))).click()
        
        # Enter email and password
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("user@test.com")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("testuser")

        # Submit
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        # Verify welcome message
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Welcome!']")))
        
if __name__ == '__main__':
    unittest.main()