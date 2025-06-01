import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")
        
    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Confirm success by checking the "Log out" button is present in the top navigation that the text
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#']")))

        # Use selectors strictly from html_data
        email = self.driver.find_element_by_name("Email")
        password = self.driver.find_element_by_name("Password")

        # Enter the login credentials
        email.send_keys("admin@admin.com")
        password.send_keys("admin")
        
        # Click on the "Login" button
        login_button = self.driver.find_element_by_css_selector(".button-1.login-button")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(login_button))
        login_button.click()

        # Check if the user is successfully logged in
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#']")))

        self.fail("Login test failed")

if __name__ == '__main__':
    unittest.main()