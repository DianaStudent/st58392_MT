from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ArtPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        try:
            # Verify header is visible
            self.wait.until(EC.visibility_of_element_located((By.ID, "header")))

            # Verify footer is visible
            self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            
            # Verify navigation links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Verify login and register links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account")))

            # Verify search input field
            search_field = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
            
            # Verify buttons
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-unstyle")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wishlist-button-add")))

            # Interact with a button (e.g., clicking one of the product quick view buttons)
            quick_view_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".quick-view")))
            quick_view_button.click()

        except Exception as e:
            self.fail(f"Failed due to missing or invisible elements: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()