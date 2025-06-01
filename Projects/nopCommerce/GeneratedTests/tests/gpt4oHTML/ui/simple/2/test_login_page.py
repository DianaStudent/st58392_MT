import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_main_ui_components(self):
        driver = self.driver

        # Go to the login page
        driver.get("http://max/login?returnUrl=%2F")

        # Wait and check for page title
        try:
            WebDriverWait(driver, 20).until(EC.title_contains("Your store. Login"))
        except Exception as e:
            self.fail(f"Failed to load the login page or title is incorrect: {str(e)}")

        # Check for elements in the login page

        # Email input
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Email"))
            )
            self.assertTrue(email_input.is_displayed())
        except:
            self.fail("Email input field is not visible.")

        # Password input
        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Password"))
            )
            self.assertTrue(password_input.is_displayed())
        except:
            self.fail("Password input field is not visible.")

        # Login button
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "login-button"))
            )
            self.assertTrue(login_button.is_displayed())
        except:
            self.fail("Login button is not visible.")
        
        # Register button on login page
        try:
            register_button_login_page = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".register-button"))
            )
            self.assertTrue(register_button_login_page.is_displayed())
        except:
            self.fail("Register button on login page is not visible.")

        # Navigate to home page
        driver.get("http://max/")

        # Check presence of the 'Home page' link
        try:
            home_page_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Home page"))
            )
            self.assertTrue(home_page_link.is_displayed())
        except:
            self.fail("Home page link is not visible.")

        # Navigate to register page
        driver.get("http://max/register?returnUrl=%2F")

        # Check presence of the 'Register' page title
        try:
            register_page_title = driver.find_element(By.CLASS_NAME, "page-title")
            self.assertIn("Register", register_page_title.text)
        except:
            self.fail("Register page title is missing or incorrect.")

        # Navigate to search page
        driver.get("http://max/search")

        # Check presence of the search button
        try:
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            self.assertTrue(search_button.is_displayed())
        except:
            self.fail("Search button is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()