import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000')

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the visibility of main header navigation
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header not found or not visible.")

        # Check navigation links
        try:
            nav_links = header.find_elements(By.CSS_SELECTOR, '.primary-nav a')
            self.assertGreater(len(nav_links), 0, "No navigation links found.")
        except:
            self.fail("Navigation links not found or not visible.")

        # Check search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
        except:
            self.fail("Search input not found or not visible.")

        # Check banner image
        try:
            banner = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.home-slider .image-gallery-image img')))
        except:
            self.fail("Banner image not found or not visible.")

        # Check best sellers
        try:
            best_sellers = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.title')))
            self.assertIn("BEST SELLERS", best_sellers.text, "Best sellers section not present or not visible.")
        except:
            self.fail("Best sellers section not found or not visible.")

        # Check product links
        try:
            product_links = driver.find_elements(By.CSS_SELECTOR, '.products a')
            self.assertGreater(len(product_links), 0, "No product links found.")
        except:
            self.fail("Product links not found or not visible.")

        # Interact with an element - click a product and verify the URL changes
        try:
            first_product = product_links[0]
            first_product.click()
            wait.until(EC.url_contains('/category-a/'))
        except:
            self.fail("Clicking on product did not navigate to the expected page.")

if __name__ == "__main__":
    unittest.main()