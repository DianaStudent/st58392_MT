import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from unittest import TestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_login_page_elements(self):
        # Header elements
        logo = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Logo']")))
        self.assertTrue(logo.is_displayed())
        
        search_bar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "search_query_top")))
        self.assertTrue(search_bar.is_displayed())

        menu_icon = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='menu-btn']")))
        self.assertTrue(menu_icon.is_displayed())

        # Content area elements
        title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Sign In')]")))
        self.assertTrue(title.is_displayed())

        username_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
        self.assertTrue(username_field.is_displayed())

        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "passwd")))
        self.assertTrue(password_field.is_displayed())

        forgot_password_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Forgot your password?')]")))
        self.assertTrue(forgot_password_link.is_displayed())

        sign_in_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "SubmitLogin")))
        self.assertTrue(sign_in_button.is_displayed())

        already_have_account_text = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Already have an account? Sign Up')]")))
        self.assertTrue(already_have_account_text.is_displayed())

        # Social media sign-in options
        google_sign_in_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "google_login")))
        self.assertTrue(google_sign_in_button.is_displayed())

        facebook_sign_in_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "facebook_login")))
        self.assertTrue(facebook_sign_in_button.is_displayed())

        twitter_sign_in_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "twitter_login")))
        self.assertTrue(twitter_sign_in_button.is_displayed())
        
if __name__ == "__main__":
    unittest.main()