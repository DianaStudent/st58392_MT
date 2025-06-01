from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class UITests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        
        # Wait until the elements are present and visible

        try:
            # Check Header elements
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header-area"))
            )

            # Check Navigation links
            nav_links = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".main-menu a"))
            )

            # Check login/register tabs
            login_tab = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
            )
            register_tab = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Register"))
            )

            # Check Login form elements
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "email"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "password"))
            )
            repeat_password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "repeatPassword"))
            )

            # Check Register button
            register_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-box button"))
            )

            # Interaction with an element
            register_button.click()

            # Wait for any UI changes post interaction
            WebDriverWait(driver, 20).until(
                EC.url_changes("http://localhost/register")
            )
        
        except Exception as e:
            self.fail(f"UI element verification failed: {str(e)}")

if __name__ == "__main__":
    unittest.main()