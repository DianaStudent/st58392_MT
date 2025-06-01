import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080')
        # Wait for top menu to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//nav[@data-name='top-menu']")))

    def test_login(self):
        login_link = self.driver.find_element_by_xpath("//a[@href='#login']")
        login_link.click()

        # Wait for login form to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//form[@data-name='login-form']")))

        email_field = self.driver.find_element_by_name("email")
        password_field = self.driver.find_element_by_name("password")

        # Fill in login form fields
        email_field.send_keys('test@user.com')
        password_field.send_keys('test@user1')

        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        # Wait for login to complete
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@data-name='sign-out']")))

        sign_out_link = self.driver.find_element_by_xpath("//a[@data-name='sign-out']")
        self.assertIsNotNone(sign_out_link.text)
        self.assertNotEqual('', sign_out_link.text)
        self.assertEqual('Sign out', sign_out_link.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()