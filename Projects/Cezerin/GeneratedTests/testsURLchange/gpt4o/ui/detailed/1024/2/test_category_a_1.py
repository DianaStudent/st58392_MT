import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header is visible
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is not visible")

        # Check footer is visible
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        except:
            self.fail("Footer is not visible")

        # Check navigation links are visible
        nav_links = [
            (By.LINK_TEXT, "Category A"),
            (By.LINK_TEXT, "Category B"),
            (By.LINK_TEXT, "Category C"),
            (By.LINK_TEXT, "Subcategory 1"),
            (By.LINK_TEXT, "Subcategory 2"),
            (By.LINK_TEXT, "Subcategory 3")
        ]
        
        for selector in nav_links:
            try:
                nav_link = self.wait.until(EC.visibility_of_element_located(selector))
            except:
                self.fail(f"Navigation link {selector} is not visible")

        # Check search input field is visible
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        except:
            self.fail("Search input field is not visible")

        # Check that sort dropdown is visible
        try:
            sort_dropdown = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sort select')))
        except:
            self.fail("Sort dropdown is not visible")

        # Check that cart button is visible
        try:
            cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
        except:
            self.fail("Cart button is not visible")

        # Interact with the sort dropdown
        try:
            sort_dropdown.click()
            favorite_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='stock_status,price,position']")))
            favorite_option.click()
        except:
            self.fail("Unable to interact with the sort dropdown")

        # Assert mini-cart is visible
        try:
            mini_cart = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'mini-cart')))
        except:
            self.fail("Mini cart is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()