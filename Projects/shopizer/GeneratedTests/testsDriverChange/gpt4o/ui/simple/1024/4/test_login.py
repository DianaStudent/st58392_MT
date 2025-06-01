import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWebsiteUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Check header presence
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Check navigation menu
            nav_links = [
                (By.LINK_TEXT, "Home"),
                (By.LINK_TEXT, "Tables"),
                (By.LINK_TEXT, "Chairs")
            ]
            for link_text, selector in nav_links:
                link = wait.until(EC.visibility_of_element_located((selector, link_text)))
                self.assertTrue(link.is_displayed(), f"{link_text} link is not visible")
            
            # Check login form elements
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
            
            username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            self.assertTrue(username_input.is_displayed(), "Username input is not visible")
            
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            self.assertTrue(password_input.is_displayed(), "Password input is not visible")
            
            login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
            self.assertTrue(login_button.is_displayed(), "Login button is not visible")

            # Check other UI elements
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_cookies_button.is_displayed(), "Accept Cookies button is not visible")

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()