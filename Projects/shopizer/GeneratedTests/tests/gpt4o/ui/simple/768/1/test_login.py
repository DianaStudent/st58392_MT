import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        # Navigate to the login page for testing
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver
        
        # Verify header logo
        try:
            logo = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo img"))
            )
        except:
            self.fail("Logo is not visible.")

        # Verify navigation link - Home
        try:
            nav_home = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/']"))
            )
        except:
            self.fail("Home navigation link is not visible.")

        # Verify navigation link - Tables
        try:
            nav_tables = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/category/tables']"))
            )
        except:
            self.fail("Tables navigation link is not visible.")

        # Verify navigation link - Chairs
        try:
            nav_chairs = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/category/chairs']"))
            )
        except:
            self.fail("Chairs navigation link is not visible.")

        # Verify login form (Email)
        try:
            email_input = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
        except:
            self.fail("Email input field is not visible.")

        # Verify login form (Password)
        try:
            password_input = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "loginPassword"))
            )
        except:
            self.fail("Password input field is not visible.")

        # Verify login button
        try:
            login_button = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit'] span"))
            )
        except:
            self.fail("Login button is not visible.")

        # Verify footer links - Contact
        try:
            footer_contact = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/contact']"))
            )
        except:
            self.fail("Contact link is not visible in footer.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()