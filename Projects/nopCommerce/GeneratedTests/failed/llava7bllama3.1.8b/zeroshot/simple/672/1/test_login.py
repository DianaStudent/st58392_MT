from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() # Use the correct browser driver here
        self.driver.get("http://max/")

    def test_login(self):
        # Home Page before login
        self.assertEqual(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, '__RequestVerificationToken'))), None)

        # Login page
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='page-title']/h1"))).click()
        email_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'Email')))
        email_field.send_keys('admin@admin.com')
        password_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']")))
        password_field.send_keys('admin')

        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-1 login-button']")))
        login_button.click()

        # After Login
        logout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log out')))
        self.assertEqual(logout_button.text, 'Log out')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()