from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_login(self):
        self.driver.get("http://localhost:8000/dk")

        # Click Account link
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/account']"))).click()

        # Wait for login page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "username_or_email")))

        # Enter email and password
        self.driver.find_element(By.ID, "username_or_email").send_keys("user@test.com")
        self.driver.find_element(By.ID, "password").send_keys("testuser")

        # Click sign-in button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Verify welcome message is present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Welcome']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()