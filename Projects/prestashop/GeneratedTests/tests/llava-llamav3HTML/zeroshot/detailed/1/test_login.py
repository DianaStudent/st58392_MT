import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginSuccess(unittest.TestCase):
    @classmethod
    def setUp(self):
        driver_path = 'webdriver/chromeedriver'
        self.driver = webdriver.Chrome(driver_path)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        # Step 1: Open the homepage.
        self.driver.get('http://html-data.com')

        # Step 2: Click the login link from the top navigation.
        login_link = self.driver.find_element_by_name('login')
        login_link.click()

        # Wait for the login page to load.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )

        # Step 4: Fill in the email and password fields using test credentials provided.
        email = self.driver.find_element_by_name('email')
        password = self.driver.find_element_by_name('password')

        email.send_keys('test@user.com')
        password.send_keys('test@user1')

        # Step 5: Click the submit button.
        submit_button = self.driver.find_element_by_name('submit')
        submit_button.click()

        # Wait for the redirect after login.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'header'))
        )

        # Step 7: Confirm that login was successful by checking that:
        sign_out_button = self.driver.find_element_by_name('sign-out')
        username = self.driver.find_element_by_name('username')

        if not sign_out_button or not username:
            self.fail("Sign out button or username is missing")

        if sign_out_button.text != "Sign out":
            self.fail("Sign out button text is incorrect")