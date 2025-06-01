import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CategoryATest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "logo-image")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-search")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-button")))
        except:
            self.fail("Header elements are not visible")

        # Check navigation links
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category B")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category C")))
        except:
            self.fail("Navigation links are not visible")

        # Check breadcrumb
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))
        except:
            self.fail("Breadcrumb is not visible")

        # Check filter elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "attribute-filter")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "price-filter")))
        except:
            self.fail("Filter elements are not visible")

        # Check sort dropdown
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".select select")))
        except:
            self.fail("Sort dropdown is not visible")

        # Check product listings
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-name")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-price")))
        except:
            self.fail("Product listings are not visible")

        # Check footer
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-logo")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-menu")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-contacts")))
        except:
            self.fail("Footer is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()