from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Replace with your preferred browser

    def test_login(self):
        self.driver.get("http://localhost/")

        # Wait for the account icon to be clickable
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/account']"))
        )

        # Click the account icon
        self.driver.find_element(By.XPATH, "//a[@href='/account']").click()

        # Wait for the login link to be clickable
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )

        # Click the login link
        self.driver.find_element(By.LINK_TEXT, "Login").click()

        # Enter email and password on the login form
        self.driver.find_element(By.NAME, "email").send_keys("test2@user.com")
        self.driver.find_element(By.NAME, "password").send_keys("test11")

        # Click the login button
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # Wait for the page to redirect to "/my-account"
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("/my-account")
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()