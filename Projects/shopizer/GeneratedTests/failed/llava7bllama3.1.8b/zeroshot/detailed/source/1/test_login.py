from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Click on the account icon/button in the top-right
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@class='nav navbar-nav navbar-right']/li[1]/a"))
        ).click()

        # Wait for the dropdown and click the "Login" link
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        self.driver.find_element(By.LINK_TEXT, "Login").click()

        # Wait for the login form to appear
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )

        # Fill in the username and password fields using credentials
        email_field = self.driver.find_element(By.ID, "email")
        email_field.send_keys("test2@user.com")

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("test**11")

        # Click the login button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

        # Wait for redirection or page update
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))
        )

        # Confirm successful login by verifying that the current URL contains "/my-account"
        self.assertIn("/my-account", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()