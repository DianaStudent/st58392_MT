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

    def test_login(self):
        # 1. Open the home page.
        self.driver.get(html_data["home_before_login"])

        # 2. Click the "Login" link.
        login_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='page-body']//form[@action='/login?returnurl=%2F']")))
        login_link.click()

        # 3. Wait for the login page to load.
        login_page_loaded = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='__RequestVerificationToken']")))

        # 4. Enter the email and password.
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Email']")))
        email_input.send_keys("admin@admin.com")

        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']")))
        password_input.send_keys("admin")

        # 5. Click the login button to submit the form.
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-1 login-button']")))
        login_button.click()

        # 6. Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        logout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='administration']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()