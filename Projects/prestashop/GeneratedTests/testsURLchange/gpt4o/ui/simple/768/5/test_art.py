import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ArtPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Header
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Contact us link
            contact_us = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
            self.assertTrue(contact_us.is_displayed(), "Contact us link is not visible")

            # Language selector
            language_selector = self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_language_selector")))
            self.assertTrue(language_selector.is_displayed(), "Language selector is not visible")

            # Sign in link
            sign_in = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertTrue(sign_in.is_displayed(), "Sign in link is not visible")

            # Cart
            cart = self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_cart")))
            self.assertTrue(cart.is_displayed(), "Cart is not visible")

            # Search widget
            search_widget = self.wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            self.assertTrue(search_widget.is_displayed(), "Search widget is not visible")

            # Product list
            product_list = self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.assertTrue(product_list.is_displayed(), "Product list is not visible")
            
            # Footer
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")

        except Exception as e:
            self.fail(f"Failed to locate a required element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()