from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestLogin(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Open the homepage.
        self.driver.get("http://localhost/")
        
        # Click the account icon in the top navigation bar.
        account_icon = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='header-account-btn']")))
        account_icon.click()

        # Click the "Login" link.
        login_link = self.wait.until(EC.element_to_be_clickable(By.XPATH, "//ul/li/a[contains(text(),'Login')]"))
        login_link.click()

        # Fill in the email and password fields.
        email_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='userName']")))
        email_field.send_keys("test2@user.com")
        
        password_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='currentPassword']")))
        password_field.send_keys("test**11")

        # Submit the login form.
        submit_button = self.wait.until(EC.element_to_be_clickable(By.XPATH, "//button[contains(text(),'Login')]"))
        submit_button.click()

        # Confirm success by checking that the browser is redirected to a page with "/my-account" in the URL.
        self.wait.until(EC.url_contains("/my-account"))
        
if __name__ == "__main__":
    unittest.main()