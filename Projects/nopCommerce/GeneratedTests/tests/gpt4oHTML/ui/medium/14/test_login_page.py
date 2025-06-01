import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Confirming key interface elements
        try:
            # Header
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Navigation links
            nav_links = driver.find_elements(By.CSS_SELECTOR, ".top-menu.notmobile li a")
            self.assertTrue(len(nav_links) > 0, "Navigation links are not available or visible")

            # Login button
            login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ico-login")))
            self.assertTrue(login_button.is_displayed(), "Login button is not visible")

            # Search input
            search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Registration button
            reg_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ico-register")))
            self.assertTrue(reg_button.is_displayed(), "Register button is not visible")
            
        except Exception as e:
            self.fail(f"Exception while checking UI elements: {str(e)}")
        
        # Interacting with elements
        try:
            login_button.click()
            
            # Wait and verify UI update
            page_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-title")))
            self.assertIn("Welcome, Please Sign In!", page_title.text)
        
        except Exception as e:
            self.fail(f"Exception while interacting with elements: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()