import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMyAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_my_account(self):
        # Open the URL
        self.driver.get("http://localhost/")

        # Click on "3. Register" link
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//h2[normalize-space()='Register']"))).click()

        # Fill all fields for registration
        email = self.driver.find_element(By.ID, "email")
        email.send_keys("test@example.com")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("test**11")

        confirm_password = self.driver.find_element(By.ID, "confirm_password")
        confirm_password.send_keys("test**11")

        name = self.driver.find_element(By.ID, "name")
        name.send_keys("John Doe")

        # Click on submit button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))).click()

        # Check if browser is redirected to a page containing "/my-account" in the URL
        self.assertIn("/my-account", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()