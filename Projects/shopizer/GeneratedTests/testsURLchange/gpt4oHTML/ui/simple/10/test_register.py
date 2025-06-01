import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_components(self):
        driver = self.driver

        # Verify header area is present
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        except:
            self.fail("Header area not found or not visible")

        # Verify logo is present
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo a img")))
        except:
            self.fail("Logo not found or not visible")

        # Verify main menu links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Main menu links not found or not visible")

        # Verify footer area is present
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        except:
            self.fail("Footer area not found or not visible")

        # Verify login/register links
        try:
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Login/Register links not found or not visible")

        # Navigate to login page
        login_link.click()

        # Verify login form
        try:
            username_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_field = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']")
        except:
            self.fail("Login form fields or button not found or not visible")

        # Navigate to register page
        driver.get("http://localhost/register")

        # Verify register form
        try:
            email_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            password_field_reg = driver.find_element(By.NAME, "password")
            repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
            register_button = driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']")
        except:
            self.fail("Register form fields or button not found or not visible")

if __name__ == "__main__":
    unittest.main()