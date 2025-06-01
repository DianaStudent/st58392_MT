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
        self.driver.get("http://localhost/login")
    
    def test_ui_elements(self):
        driver = self.driver
        
        # Wait for navigation menu to be visible and check its presence
        nav_links = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "nav ul li a"))
        )
        self.assertEqual(len(nav_links), 3, "Navigation links are missing or incorrect.")

        # Check presence of login form inputs and buttons
        username_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        
        password_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "loginPassword"))
        )
        
        login_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
        )
        
        # Interact with "Accept Cookies" button
        try:
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Accept Cookies button interaction failed: {e}")

        # Interacting with login form to verify no errors are caused
        username_input.send_keys("test@example.com")
        password_input.send_keys("password")
        try:
            login_button.click()
        except Exception as e:
            self.fail(f"Login button interaction failed: {e}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()