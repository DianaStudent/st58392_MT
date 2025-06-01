import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestClothesPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Check for header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is not visible")

        # Check for footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(footer, "Footer is not visible")
        
        # Check for navigation bar
        nav = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        self.assertIsNotNone(nav, "Navigation bar is not visible")

        # Check for search input visibility
        search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
        self.assertIsNotNone(search_input, "Search input is not visible")

        # Check for sign in link
        sign_in_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        self.assertIsNotNone(sign_in_link, "Sign in link is not visible")
        
        # Check for all category links
        categories = ['Home', 'Clothes', 'Accessories', 'Art']
        for category in categories:
            category_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, category)))
            self.assertIsNotNone(category_link, f"{category} link is not visible")

        # Check for product list
        products = self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        self.assertIsNotNone(products, "Product list is not visible")

        # Interact with the search input
        search_input.clear()
        search_input.send_keys("T-shirt")
        
        # Click on a button and ensure UI reacts
        search_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.material-icons.search")))
        self.assertIsNotNone(search_button, "Search button is not visible")
        search_button.click()
        
        # Asserting a change in UI (results should show updated)
        search_results = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products")))
        self.assertIsNotNone(search_results, "Search results are not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()