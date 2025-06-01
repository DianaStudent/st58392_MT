import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIAutomation(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # 1. Check presence of navigation links
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        except Exception as e:
            self.fail(f"Navigation links are missing or not visible: {str(e)}")
        
        # 2. Check presence of 'Sign in' button
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except Exception as e:
            self.fail(f"'Sign in' button is missing or not visible: {str(e)}")
        
        # 3. Check presence of search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search']")))
        except Exception as e:
            self.fail(f"Search input is missing or not visible: {str(e)}")
        
        # 4. Check presence of language dropdown
        try:
            language_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".language-selector button")))
        except Exception as e:
            self.fail(f"Language dropdown is missing or not visible: {str(e)}")
        
        # Interact with 'Sign in' button and check no errors
        try:
            sign_in_button.click()
            wait.until(EC.url_contains("login"))
        except Exception as e:
            self.fail(f"Error interacting with 'Sign in' button: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()