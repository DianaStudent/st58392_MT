import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Use the Chrome driver if you have it installed
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        try:
            email_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys("user@test.com")
            
            password_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys("testuser")

            go_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            go_button.click()

            # Wait for the login to be successful and welcome message to appear
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "welcome-message"))
            )
        except TimeoutException:
            self.fail("Login was not successful.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()