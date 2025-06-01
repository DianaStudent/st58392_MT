from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://localhost/'

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'shoppee')))
            self.assertEqual('shoppee', self.driver.title)

            account_icon = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Account')]")))
            )
            login_link = WebDriverWait(account_icon, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]")))
            account_icon.click()
            self.wait_for_page_load()

            login_form = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//form[@id='my-login']")))
            email_field = WebDriverWait(login_form, 20).until(
                EC.visibility_of_element_located((By.ID, 'email')))
            password_field = WebDriverWait(login_form, 20).until(
                EC.visibility_of_element_located((By.ID, 'password')))
            email_field.send_keys('test2@user.com')
            password_field.send_keys('test11')

            login_button = WebDriverWait(login_form, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary')]")))
            self.wait_for_page_load()

            success_message = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'success-message')))
            self.assertEqual('Login Successful', success_message.text)

        except Exception as e:
            print(f'An error occurred during the test: {str(e)}')

if __name__ == '__main__':
    unittest.main()