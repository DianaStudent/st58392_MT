from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AccessoriesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_key_ui_elements(self):
        driver = self.driver
        
        # Verify structural elements are visible
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))
        except Exception as e:
            self.fail(f"Failed to find structural elements: {str(e)}")

        # Verify input fields, buttons, and links
        try:
            # Verify search box
            search_box = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))

            # Verify navigation links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Verify buttons
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-unstyle")))

            # Verify product elements
            product_items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-miniature")))

            # Verify presence of a specific product
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Mug The adventure begins")))

            # Verify cart icon
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-products-count")))
        except Exception as e:
            self.fail(f"Failed to find input fields, buttons, or links: {str(e)}")

        # Interact with key UI elements
        try:
            # Simulate search
            search_box.send_keys("Mug")
            submit_search = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".material-icons.search")))
            submit_search.click()
        except Exception as e:
            self.fail(f"Failed to interact with search functionality: {str(e)}")

        # Confirm UI reacts visually
        try:
            # Verify search results
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products")))
        except Exception as e:
            self.fail(f"Failed to confirm UI reaction: {str(e)}")

# Run the test
if __name__ == '__main__':
    unittest.main()