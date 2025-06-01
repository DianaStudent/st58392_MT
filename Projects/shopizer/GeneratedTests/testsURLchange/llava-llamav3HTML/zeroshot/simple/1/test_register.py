import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import Assertions
from selenium.webdriver.common.alert import Alert

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        # Open the registration page
        url = "http://localhost/"
        self.driver.get(url)

        # Get the email field and enter a dynamically generated email address
        email_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_address = Assertions.getRandomEmail()
        email_field.send_keys(email_address)

        # Get the password fields and enter the password and repeat password values
        password_field1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "password1"))
        )
        password1 = Assertions.getRandomPassword()
        password_field1.send_keys(password1)
        password_field2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "repeat_password"))
        )
        password2 = Assertions.getRandomPassword()
        password_field2.send_keys(password2)

        # Get the checkbox field and select it
        checkbox_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "agree_t_and_c"))
        )
        checkbox_field.click()

        # Submit the form to register the account
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "register_submit"))
        )
        submit_button.send_keys(Keys.RETURN)

        # Wait for the success message to appear and check that it contains the correct URL
        success_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'success')]/a"))
        )
        url_after_redirect = self.driver.current_url

        Assertions.assertTrue(success_message, "The registration failed")
        Assertions.assertTrue(url_after_redirect, "The browser was not redirected to the account management page")

if __name__ == '__main__':
    unittest.main()