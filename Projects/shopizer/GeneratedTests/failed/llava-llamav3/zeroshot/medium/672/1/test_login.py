from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class TestMyAccountLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_my_account_login(self):
        # Step 1: Open the homepage.
        self.driver.get("http://localhost/")

        # Step 2: Click the account icon in the top navigation bar.
        account_icon = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_css_selector(".shopper-account-icon"))
        account_icon.click()

        # Step 3: Click the "Login" link.
        login_link = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_css_selector(".login-link"))
        login_link.click()

        # Step 4: Fill in the email and password fields.
        email_field = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name("email"))
        password_field = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name("password"))

        email_field.send_keys("test2@user.com")
        password_field.send_keys("test11")

        # Step 5: Submit the login form.
        submit_button = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_css_selector(".login-button"))
        submit_button.click()

        # Confirm success by checking that the browser is redirected to a page containing "/my-account" in the URL.
        my_account_url = WebDriverWait(self.driver, 20).until(
            lambda x: x.current_url())
        self.assertTrue("/my-account" in my_account_url)

if __name__ == '__main__':
    unittest.main()
```