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
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://localhost/login")

        # Wait for the header to be visible
        try:
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area"))
            )
        except:
            self.fail("Header not found or not visible")

        # Check footer visibility
        try:
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area"))
            )
        except:
            self.fail("Footer not found or not visible")

        # Check main menu and buttons visibility
        try:
            nav_menu = driver.find_element(By.CSS_SELECTOR, "div.main-menu")
            self.assertTrue(nav_menu.is_displayed(), "Main navigation menu not visible")

            login_button = driver.find_element(By.LINK_TEXT, "Login")
            register_button = driver.find_element(By.LINK_TEXT, "Register")

            self.assertTrue(login_button.is_displayed(), "Login button not visible")
            self.assertTrue(register_button.is_displayed(), "Register button not visible")
        except:
            self.fail("Navigation or buttons missing")

        # Check login form fields
        try:
            email_input = driver.find_element(By.NAME, "email")
            password_input = driver.find_element(By.NAME, "password")
            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            register_submit_button = driver.find_element(By.CSS_SELECTOR, "div.button-box button[type='submit']")

            self.assertTrue(email_input.is_displayed(), "Email input not visible")
            self.assertTrue(password_input.is_displayed(), "Password input not visible")
            self.assertTrue(repeat_password_input.is_displayed(), "Repeat Password input not visible")
            self.assertTrue(register_submit_button.is_displayed(), "Register button not visible")
        except:
            self.fail("Form fields missing")

        # Interact with elements
        try:
            register_button.click()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.login-register-wrapper"))
            )
        except:
            self.fail("Form interaction failed or did not produce expected outcome")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()