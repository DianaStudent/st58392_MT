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
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        # Check if header elements are present and visible
        try:
            header_logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo a img")))
            self.assertTrue(header_logo.is_displayed(), "Header logo not displayed")
        except Exception as e:
            self.fail(f"Header logo not found or not visible: {str(e)}")

        try:
            nav_home = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertTrue(nav_home.is_displayed(), "Home link not displayed in navigation")
        except Exception as e:
            self.fail(f"Home link not found or not visible: {str(e)}")

        try:
            nav_tables = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.assertTrue(nav_tables.is_displayed(), "Tables link not displayed in navigation")
        except Exception as e:
            self.fail(f"Tables link not found or not visible: {str(e)}")

        try:
            nav_chairs = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            self.assertTrue(nav_chairs.is_displayed(), "Chairs link not displayed in navigation")
        except Exception as e:
            self.fail(f"Chairs link not found or not visible: {str(e)}")

        # Check if login/register links are present and visible
        try:
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            self.assertTrue(login_link.is_displayed(), "Login link not displayed")
        except Exception as e:
            self.fail(f"Login link not found or not visible: {str(e)}")

        try:
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(register_link.is_displayed(), "Register link not displayed")
        except Exception as e:
            self.fail(f"Register link not found or not visible: {str(e)}")

        # Check if cookie consent button is present and visible
        try:
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button not displayed")
        except Exception as e:
            self.fail(f"Accept cookies button not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()