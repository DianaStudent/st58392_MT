from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import Assert

class TestLogin(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        
    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("http://localhost:8080/en/")
        login_link = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//a[@data-name='login']")
        )
        login_link.click()
        
        email_field = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//input[@id='email']")
        password_field = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//input[@id='password']")
        
        credentials = {"Email": "test@user.com", "Password": "test@user1"}
        for key, value in credentials.items():
            getattr(email_field, 'send_keys')(value)
            getattr(password_field, 'send_keys')('')

        login_button = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//button[@data-name='login']")
        login_button.click()

        sign_out_text = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//span[@data-name='sign-out']")
        assert "Sign out" in sign_out_text

if __name__ == '__main__':
    unittest.main()