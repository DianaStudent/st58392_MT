import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver

        # Check Header elements
        self.assert_element_visible(By.CSS_SELECTOR, "header#header")

        # Contact us link
        self.assert_element_visible(By.LINK_TEXT, "Contact us")

        # Language selector
        self.assert_element_visible(By.CSS_SELECTOR, "div.language-selector")

        # Sign in link
        self.assert_element_visible(By.LINK_TEXT, "Sign in")

        # Cart
        self.assert_element_visible(By.CSS_SELECTOR, "div#_desktop_cart")

        # Navigation links
        self.assert_element_visible(By.LINK_TEXT, "Clothes")
        self.assert_element_visible(By.LINK_TEXT, "Accessories")
        self.assert_element_visible(By.LINK_TEXT, "Art")

        # Main Content
        self.assert_element_visible(By.CSS_SELECTOR, "section#main h1.h1")

        # Subcategories
        self.assert_element_visible(By.CSS_SELECTOR, "div#subcategories")

        # Product list
        self.assert_element_visible(By.CSS_SELECTOR, "div#js-product-list")

        # Product items
        products = driver.find_elements(By.CSS_SELECTOR, "div.js-product")
        self.assertTrue(len(products) > 0, "No products found")

        # Footer
        self.assert_element_visible(By.CSS_SELECTOR, "footer#footer")
    
    def assert_element_visible(self, by, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            self.assertTrue(element.is_displayed(), f"Element {value} is not visible")
        except Exception as e:
            self.fail(f"Element not found or not visible: {value}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()