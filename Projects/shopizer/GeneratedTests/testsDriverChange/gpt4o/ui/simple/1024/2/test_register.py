import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header elements
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except Exception as e:
            self.fail(f"Header elements not present or visible: {e}")

        # Verify cookie consent button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located(
                (By.ID, "rcc-confirm-button")))
        except Exception as e:
            self.fail(f"Cookie consent button not present or visible: {e}")

        # Verify login form elements
        try:
            email_field = wait.until(EC.visibility_of_element_located(
                (By.NAME, "email")))
            password_field = wait.until(EC.visibility_of_element_located(
                (By.NAME, "password")))
            repeat_password_field = wait.until(EC.visibility_of_element_located(
                (By.NAME, "repeatPassword")))
            first_name_field = wait.until(EC.visibility_of_element_located(
                (By.NAME, "firstName")))
            last_name_field = wait.until(EC.visibility_of_element_located(
                (By.NAME, "lastName")))
            register_button = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button[type='submit']")))
        except Exception as e:
            self.fail(f"Form elements not present or visible: {e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()