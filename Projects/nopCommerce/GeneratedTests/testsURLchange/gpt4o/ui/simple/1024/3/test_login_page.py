import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver

        # Check for header elements
        try:
            header_logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-logo img")))
            search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box-button")))
            header_links = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-links")))
        except Exception as e:
            self.fail(f"Header elements not found or not visible: {e}")

        # Check for login form
        try:
            email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-button")))
            register_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".register-button")))
            remember_me_checkbox = self.wait.until(EC.visibility_of_element_located((By.ID, "RememberMe")))
        except Exception as e:
            self.fail(f"Login form elements not found or not visible: {e}")

        # Check for footer elements
        try:
            footer_info = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-info")))
            follow_us = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "follow-us")))
            newsletter_input = self.wait.until(EC.visibility_of_element_located((By.ID, "newsletter-email")))
        except Exception as e:
            self.fail(f"Footer elements not found or not visible: {e}")

if __name__ == "__main__":
    unittest.main()