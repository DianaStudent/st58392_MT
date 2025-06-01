from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestAccountLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080")  # replace with your URL

    def test_account_login(self):
        # Click account icon and then click the "Login" link to open the login form
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/my-account']"))).click()
        self.driver.find_element(By.LINK_TEXT, 'Login').click()

        # Check that the browser is redirected to a page containing "/my-account" in the URL
        current_url = self.driver.current_url
        self.assertIn("/my-account", current_url)

        # Fill login form
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'email')))
        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'password')))

        email_input.send_keys("test2@user.com")
        password_input.send_keys("test11")

        # Submit login form
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()