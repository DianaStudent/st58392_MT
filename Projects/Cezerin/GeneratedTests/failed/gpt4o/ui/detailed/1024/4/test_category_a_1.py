from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryA1Page(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/category-a-1")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header presence
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(header, "Header is missing")

        # Check footer presence
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        self.assertIsNotNone(footer, "Footer is missing")

        # Check main navigation links
        nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul.nav-level-0 a")))
        self.assertGreater(len(nav_links), 0, "Navigation links are missing")

        # Check search input field
        search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
        self.assertIsNotNone(search_box, "Search input field is missing")

        # Check presence of sort select element
        sort_select = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select")))
        self.assertIsNotNone(sort_select, "Sort select is missing")

        # Check presence of filter button (for mobile)
        try:
            filter_button = driver.find_element(By.CSS_SELECTOR, "button.is-fullwidth")
            self.assertTrue(filter_button.is_displayed(), "Filter button is missing")
        except:
            self.fail("Filter button is missing")

        # Check if category and breadcrumb titles are present
        breadcrumb = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.breadcrumb")))
        self.assertIsNotNone(breadcrumb, "Breadcrumb navigation is missing")

        category_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.category-title")))
        self.assertIsNotNone(category_title, "Category title is missing")

        # Check if the cart button is present and clickable
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cart-button img")))
        self.assertIsNotNone(cart_button, "Cart button is missing")
        cart_button.click()

        # Confirm cart button click reaction (e.g., mini-cart visibility)
        mini_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.mini-cart")))
        self.assertIsNotNone(mini_cart, "Mini cart did not appear after clicking cart button")

if __name__ == "__main__":
    unittest.main()