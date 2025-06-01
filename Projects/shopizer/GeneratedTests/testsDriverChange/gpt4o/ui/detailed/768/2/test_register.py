import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_presence_of_elements(self):
        driver = self.driver

        # Wait for Header
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "header-area"))
        )
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Wait for Footer
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "footer-area"))
        )
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Wait for Main Navigation
        main_menu = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.main-menu ul"))
        )
        self.assertTrue(main_menu.is_displayed(), "Main navigation is not visible")

        # Wait for Login form
        email_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        self.assertTrue(email_field.is_displayed(), "Email input is not visible")

        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        self.assertTrue(password_field.is_displayed(), "Password input is not visible")

        # Check for login button
        login_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.button-box button[type='submit']"))
        )
        self.assertTrue(login_button.is_displayed(), "Login button is not visible")

        # Interact with Accept Cookies button
        accept_cookies_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        )
        self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")
        accept_cookies_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()