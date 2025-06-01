import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CategoryATest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except Exception:
            self.fail("Header is not visible")

        # Check presence of logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo-image')))
        except Exception:
            self.fail("Logo is not visible")

        # Check navigation links
        nav_links = ['Category A', 'Category B', 'Category C']
        for nav in nav_links:
            try:
                link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, nav)))
            except Exception:
                self.fail(f"Navigation link {nav} is not visible")

        # Check search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        except Exception:
            self.fail("Search input is not visible")

        # Check presence of sort dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'select')))
        except Exception:
            self.fail("Sort dropdown is not visible")

        # Check presence of products
        products = ['Product A', 'Product B']
        for product in products:
            try:
                product_element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, product)))
            except Exception:
                self.fail(f"Product {product} is not visible")

        # Interact with elements
        # Click on 'Product A' and verify presence of price
        try:
            product_a_link = driver.find_element(By.LINK_TEXT, 'Product A')
            product_a_link.click()
            price = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '$950.00')]")))
        except Exception:
            self.fail("Interacting with Product A failed or price not visible")

        # Check no errors
        self.assertFalse(self.driver.find_elements(By.CLASS_NAME, 'error'))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()