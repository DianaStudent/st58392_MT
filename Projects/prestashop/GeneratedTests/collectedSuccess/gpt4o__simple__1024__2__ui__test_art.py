from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class ArtPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_visible(self):
        driver = self.driver

        try:
            # Check header
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header, "Header is not visible")

            # Check breadcrumb
            breadcrumb = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))
            self.assertIsNotNone(breadcrumb, "Breadcrumb is not visible")

            # Check product list
            product_list = self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.assertIsNotNone(product_list, "Product list is not visible")

            # Check filters section
            filters_section = self.wait.until(EC.visibility_of_element_located((By.ID, "search_filters_wrapper")))
            self.assertIsNotNone(filters_section, "Filters section is not visible")

            # Check search bar
            search_bar = self.wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            self.assertIsNotNone(search_bar, "Search bar is not visible")

            # Check language selector
            language_selector = self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_language_selector")))
            self.assertIsNotNone(language_selector, "Language selector is not visible")

            # Check sign in link
            sign_in_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertIsNotNone(sign_in_link, "Sign in link is not visible")

            # Check cart icon
            cart_icon = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
            self.assertIsNotNone(cart_icon, "Cart icon is not visible")

            # Check each product within product list
            products = driver.find_elements(By.CLASS_NAME, "product-miniature")
            self.assertGreater(len(products), 0, "No products visible on the page")

        except Exception as e:
            self.fail(f"An expected UI element is missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()