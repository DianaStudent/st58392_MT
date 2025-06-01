import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/login")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
            self.assertTrue(header.is_displayed(), "Header is not displayed.")
        except Exception:
            self.fail("Header element is missing.")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
            self.assertTrue(footer.is_displayed(), "Footer is not displayed.")
        except Exception:
            self.fail("Footer element is missing.")
        
        # Check navigation links
        try:
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//nav//a")))
            self.assertTrue(len(nav_links) >= 3, "Not all navigation links are visible.")
        except Exception:
            self.fail("Navigation links are missing.")
        
        # Check input fields are visible
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            self.assertTrue(email_input.is_displayed(), "Email input is not visible.")
        except Exception:
            self.fail("Email input field is missing.")

        try:
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            self.assertTrue(password_input.is_displayed(), "Password input is not visible.")
        except Exception:
            self.fail("Password input field is missing.")

        # Check buttons are visible
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))
            self.assertTrue(login_button.is_displayed(), "Login button is not visible.")
        except Exception:
            self.fail("Login button is missing.")

        try:
            register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']")))
            self.assertTrue(register_button.is_displayed(), "Register button is not visible.")
        except Exception:
            self.fail("Register button is missing.")

        # Interaction: Click "Accept Cookies" button
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
            # Check UI reaction if applicable
        except Exception:
            self.fail("Accept cookies button is missing or not clickable.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()