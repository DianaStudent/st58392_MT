import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_login(self):
        # Open the homepage
        self.driver.get("http://localhost/")

        # Click the account icon in the top navigation bar
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='account']"))).click()

        # Click the "Login" link
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

        # Fill in the email and password fields
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
        email_field.send_keys("test2@user.com")

        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.send_keys("test**11")

        # Submit the login form
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        # Confirm success by checking that the browser is redirected to a page with "/my-account" in the URL
        current_url = self.driver.current_url
        self.assertIn("/my-account", current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()