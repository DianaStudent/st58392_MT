from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIComponents(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver

        # Load the homepage
        driver.get("http://max/")

        # Checking for header elements
        try:
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header"))
            )
            self.assertTrue(header.is_displayed(), "Header element is not visible.")
        except:
            self.fail("Header element is missing.")

        # Checking for navigation links
        try:
            navbar = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header-links"))
            )
            self.assertTrue(navbar.is_displayed(), "Navigation links are not visible.")
        except:
            self.fail("Navigation links are missing.")
        
        # Checking for footer elements
        try:
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "footer"))
            )
            self.assertTrue(footer.is_displayed(), "Footer element is not visible.")
        except:
            self.fail("Footer element is missing.")

        # Navigate to the login page
        driver.get("http://max/login?returnUrl=%2F")
        
        # Check for login page form elements
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Email"))
            )
            self.assertTrue(email_input.is_displayed(), "Email input field is not visible.")
        except:
            self.fail("Email input field is missing.")

        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Password"))
            )
            self.assertTrue(password_input.is_displayed(), "Password input field is not visible.")
        except:
            self.fail("Password input field is missing.")
        
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "login-button"))
            )
            self.assertTrue(login_button.is_displayed(), "Login button is not visible.")
        except:
            self.fail("Login button is missing.")

        # Navigate to the register page and check elements
        driver.get("http://max/register?returnUrl=%2F")
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "register-button"))
            )
            self.assertTrue(register_button.is_displayed(), "Register button is not visible.")
        except:
            self.fail("Register button is missing.")

        # Navigate to the search page
        driver.get("http://max/search")
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "small-searchterms"))
            )
            self.assertTrue(search_input.is_displayed(), "Search input field is not visible.")
        except:
            self.fail("Search input field is missing.")

        try:
            search_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button"))
            )
            self.assertTrue(search_button.is_displayed(), "Search button is not visible.")
        except:
            self.fail("Search button is missing.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()