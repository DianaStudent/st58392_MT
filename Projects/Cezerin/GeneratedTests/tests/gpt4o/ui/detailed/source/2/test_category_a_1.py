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

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertIsNotNone(header, "Header is missing")

        # Check footer
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer is missing")

        # Check navigation links
        nav_links = [
            ("Category A", "/category-a"),
            ("Category B", "/category-b"),
            ("Category C", "/category-c")
        ]
        for name, url in nav_links:
            link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, name)))
            self.assertIsNotNone(link, f"Navigation link {name} is missing")
            self.assertEqual(link.get_attribute('href'), f"http://localhost:3000{url}")

        # Check search input field
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
        self.assertIsNotNone(search_input, "Search input field is missing")

        # Check category title
        category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'category-title')))
        self.assertIsNotNone(category_title, "Category title is missing")

        # Check sort dropdown
        sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select')))
        self.assertIsNotNone(sort_dropdown, "Sort dropdown is missing")

        # Check if Sort button is clickable
        sort_title = driver.find_element(By.CLASS_NAME, "sort-title").text
        self.assertEqual(sort_title.strip(), "Sort:", "Sort button title is incorrect")

        # Check if loading products is visible
        products_section = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'section-category')))
        self.assertIsNotNone(products_section, "Products section is missing")

        # Check cart icon
        cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.cart-button')))
        self.assertIsNotNone(cart_icon, "Cart icon is missing")

        # Check if the cart modal can be opened
        cart_icon.click()
        cart_modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'mini-cart')))
        self.assertIn("Your cart is empty", cart_modal.text, "Cart modal is not displaying correctly")

if __name__ == "__main__":
    unittest.main()