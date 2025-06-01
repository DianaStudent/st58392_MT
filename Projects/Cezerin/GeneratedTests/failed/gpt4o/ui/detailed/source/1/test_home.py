from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_homepage_elements(self):
        # Check header
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        if not header.is_displayed():
            self.fail("Header is not visible")

        # Check footer
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        if not footer.is_displayed():
            self.fail("Footer is not visible")

        # Check main navigation links
        categories = ["Category A", "Category B", "Category C"]
        for category in categories:
            nav_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, category)))
            if not nav_link.is_displayed():
                self.fail(f"Navigation link for {category} is not visible")

        # Check search input
        search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
        if not search_input.is_displayed():
            self.fail("Search input field is not visible")

        # Check Best Sellers section
        best_sellers = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title')))
        if not best_sellers.is_displayed():
            self.fail("Best Sellers section is not visible")

        # Check product links
        products = ["Product A", "Product B"]
        for product in products:
            product_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, product)))
            if not product_link.is_displayed():
                self.fail(f"Product link for {product} is not visible")

        # Interact with search functionality
        search_input.send_keys("Test")
        search_icon = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-icon-search')))
        search_icon.click()

        # Verify cart button
        cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
        if not cart_button.is_displayed():
            self.fail("Cart button is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()