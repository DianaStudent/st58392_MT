import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Step 1: Open the homepage.
        self.driver.get("http://localhost/")

        # Wait for the account icon to be clickable and click it
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/my-account']"))).click()

        # Click the "Login" link.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login'))).click()

        # Fill in the email and password fields.
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        email_input.send_keys("test2@user.com")

        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        password_input.send_keys("test**11")

        # Submit the login form.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        # Confirm success by checking that the browser is redirected to a page containing "/my-account" in the URL
        current_url = self.driver.current_url
        self.assertIn('/my-account', current_url)


if __name__ == "__main__":
    unittest.main()