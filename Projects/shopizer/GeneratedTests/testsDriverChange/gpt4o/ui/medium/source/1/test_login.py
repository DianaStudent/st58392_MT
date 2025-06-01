import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsiteUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
    
    def test_ui_elements(self):
        driver = self.driver

        # Check navigation links
        nav_links_text = ["Home", "Tables", "Chairs"]
        for link_text in nav_links_text:
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.LINK_TEXT, link_text))
                )
            except:
                self.fail(f"Navigation link '{link_text}' not found or not visible.")

        # Check login form fields
        try:
            username_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "loginPassword"))
            )
        except:
            self.fail("Login form fields are not found or not visible.")
        
        # Check login button
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']"))
            )
        except:
            self.fail("Login button is not found or not visible.")

        # Interact with elements
        try:
            username_input.send_keys("test@example.com")
            password_input.send_keys("password")
            login_button.click()

            # Verify no errors and UI updates
            WebDriverWait(driver, 20).until(EC.url_changes("http://localhost/login"))
        except Exception as e:
            self.fail(f"Interaction with login elements failed: {e}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()