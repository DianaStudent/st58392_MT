import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header is visible
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertIsNotNone(header, "Header is missing from the page.")

        # Check logo is visible
        logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo-image')))
        self.assertIsNotNone(logo, "Logo is missing from the page.")

        # Check search input field is visible
        search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        self.assertIsNotNone(search_input, "Search input field is missing from the page.")

        # Check cart button is visible
        cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
        self.assertIsNotNone(cart_button, "Cart button is missing from the page.")

        # Check navigation links are visible
        nav_links = driver.find_elements(By.CSS_SELECTOR, '.primary-nav .cat-parent a')
        self.assertGreater(len(nav_links), 0, "Navigation links are missing from the page.")
        for nav_link in nav_links:
            self.assertTrue(nav_link.is_displayed(), "A navigation link is not visible.")

        # Check 'BEST SELLERS' section is visible
        best_sellers_title = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='BEST SELLERS']"))
        )
        self.assertIsNotNone(best_sellers_title, "'BEST SELLERS' section is missing from the page.")

        # Check products are visible in 'BEST SELLERS'
        best_sellers_products = driver.find_elements(By.CLASS_NAME, 'product-caption')
        self.assertGreater(len(best_sellers_products), 0, "No products found in 'BEST SELLERS' section.")
        for product in best_sellers_products:
            self.assertTrue(product.is_displayed(), "A product in 'BEST SELLERS' is not visible.")

        # Check footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer is missing from the page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()