import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class ClothesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        
        # Wait for and check presence of main UI components
        try:
            # Header
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            # Navigation Links
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Search input
            search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text'][@name='s']")))

            # Subcategories
            subcategories = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "subcategories-list")))

            # Products
            products = self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))

            # Cart button
            cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))

            # Footer
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))

            # Interact with an element to ensure UI updates
            cart_button.click()

            # Optionally verify UI updates after interaction
            cart_text = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-products-count")))
            self.assertIn("(0)", cart_text.text)

        except Exception as e:
            self.fail(f"UI element not found or visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()