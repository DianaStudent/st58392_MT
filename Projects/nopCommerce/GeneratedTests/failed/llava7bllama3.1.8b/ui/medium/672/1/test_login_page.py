from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_login_page_elements(self):
        # Navigation links
        nav_links = self.driver.find_elements(By.XPATH, "//ul[@class='nav']/li")
        self.assertGreater(len(nav_links), 0)

        # Inputs
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'email')))
        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'password')))

        # Buttons
        sign_in_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        forget_password_link = self.driver.find_element(By.XPATH, "//a[text()='Forget Password?']")

        # Banners
        welcome_message_banner = self.driver.find_element(By.XPATH, "//h2[contains(text(), 'Welcome to New Reality Commerce')]")

    def test_login_button_click(self):
        sign_in_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        sign_in_button.click()

        # Verify UI updates visually
        self.assertTrue(sign_in_button.is_enabled())
        self.assertEqual(sign_in_button.get_attribute('value'), 'Sign In')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()