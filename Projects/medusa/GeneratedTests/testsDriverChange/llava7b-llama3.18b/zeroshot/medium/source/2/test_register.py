import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Account"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Join Us']"))).click()

    def test_registration_success(self):
        first_name = self.driver.find_element(By.NAME, "first_name")
        last_name = self.driver.find_element(By.NAME, "last_name")
        email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
        password = self.driver.find_element(By.NAME, "password")
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='SUBMIT']")))

        first_name.send_keys("user")
        last_name.send_keys("test")
        email.send_keys("registered_user_" + str(12345) + "@example.com") # Generate a unique email for each test run
        password.send_keys("testuser")

        submit_button.click()

        welcome_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Welcome']")))
        self.assertTrue(welcome_message.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()