import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check the header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible")

        # Check for the 'Contact us' link
        try:
            contact_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#contact-link a")))
        except:
            self.fail("Contact us link is not visible")

        # Check for the 'Sign in' link
        try:
            sign_in = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Sign in link is not visible")
        
        # Check for the 'Cart' button
        try:
            cart_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-preview .shopping-cart")))
        except:
            self.fail("Cart button is not visible")

        # Check language dropdown
        try:
            language_dropdown = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".language-selector-wrapper .dropdown")))
        except:
            self.fail("Language dropdown is not visible")

        # Check the search form
        try:
            search_form = self.wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
        except:
            self.fail("Search form is not visible")

        # Check main category menu
        try:
            category_menu = self.wait.until(EC.visibility_of_element_located((By.ID, "top-menu")))
        except:
            self.fail("Category menu is not visible")

        # Check for the 'Art' section title
        try:
            art_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h1")))
        except:
            self.fail("Art section title is not visible")

        # Check for the product list
        try:
            product_list = self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        except:
            self.fail("Product list is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()