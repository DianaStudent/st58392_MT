import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_login(self):
        # Open the home page
        self.driver.get(html_data["home_before_login"])

        # Click the "Login" link
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login?returnurl=%2F']")))
        login_link.click()

        # Wait for the login page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='Email']")))

        # Enter email and password
        email_input = self.driver.find_element_by_xpath("//input[@name='Email']")
        if not email_input:
            self.fail("Element 'Email' is missing")

        email_input.send_keys(html_data["credentials"]["Email"])
        
        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@data-val-required='The Password field is required.']")))
        if not password_input:
            self.fail("Element 'Password' is missing")

        password_input.send_keys(html_data["credentials"]["Password"])

        # Click the login button
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-1 login-button']")))
        login_button.click()

        # Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        try:
            logout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='administration']")))
        except TimeoutException:
            self.fail("Logout button not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()