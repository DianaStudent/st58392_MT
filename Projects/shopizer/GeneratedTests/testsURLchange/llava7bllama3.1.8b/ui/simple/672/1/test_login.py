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
        self.driver.get("http://localhost/login")

    def test_login_page_elements(self):
        # Check header and title
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))
        self.assertTrue(header.is_displayed())

        # Check username field
        username_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))
        self.assertTrue(username_field.is_displayed())

        # Check password field
        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
        self.assertTrue(password_field.is_displayed())

        # Check login button
        login_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        self.assertTrue(login_button.is_displayed())

        # Check remember me checkbox
        remember_me_checkbox = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "remember_me")))
        self.assertTrue(remember_me_checkbox.is_displayed())

        # Check sign up link
        sign_up_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "SIGN UP")))
        self.assertTrue(sign_up_link.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()