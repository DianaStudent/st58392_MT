import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(header, "Header is not present or not visible")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        self.assertIsNotNone(footer, "Footer is not present or not visible")

        # Check main navigation
        main_nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".primary-nav")))
        self.assertIsNotNone(main_nav, "Main navigation is not present or not visible")

        # Check search box presence
        search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box input")))
        self.assertIsNotNone(search_box, "Search box is not present or not visible")

        # Check category links
        categories = driver.find_elements(By.CSS_SELECTOR, ".primary-nav a")
        self.assertTrue(categories, "Category links are missing")

        # Interact by clicking the first category link
        categories[0].click()

        # Confirm the UI reacts by checking if a URL change occurs
        wait.until(EC.url_contains("category-a"), "Category A page did not load")

        # Check products section visibility
        products_section = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".products")))
        self.assertIsNotNone(products_section, "Products section is not present or not visible")

        # Check presence of a product link
        product_links = driver.find_elements(By.CSS_SELECTOR, ".products a")
        self.assertTrue(product_links, "Product links are missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()