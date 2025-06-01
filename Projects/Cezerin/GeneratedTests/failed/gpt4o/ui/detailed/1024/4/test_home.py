from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebPageElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check presence of header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header not found")

        # Check presence of footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        except:
            self.fail("Footer not found")

        # Check presence of navigation links
        try:
            nav_links = header.find_elements(By.CSS_SELECTOR, ".primary-nav ul li div.cat-parent a")
            self.assertTrue(all(link.is_displayed() for link in nav_links), "Some navigation links are not visible")
        except:
            self.fail("Navigation links not found")

        # Check presence of search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
        except:
            self.fail("Search input not found")

        # Check presence of the search button
        try:
            search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-icon-search")))
        except:
            self.fail("Search button not found")

        # Check presence of product section
        try:
            product_section = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".products.is-centered")))
            product_items = product_section.find_elements(By.CSS_SELECTOR, ".product-name")
            self.assertTrue(all(item.is_displayed() for item in product_items), "Some products are not visible")
        except:
            self.fail("Product section or some products not found")

        # Ensure cart button is present
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button")))
        except:
            self.fail("Cart button not found")

        # Interact with navigation - click Category A
        try:
            category_a_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/category-a"]')))
            category_a_link.click()

            # Confirm page navigation
            current_url = driver.current_url
            self.assertEqual(current_url, "http://localhost:3000/category-a", "Navigation to Category A failed")
        except:
            self.fail("Category A link not found or interaction failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()