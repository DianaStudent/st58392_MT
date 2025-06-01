import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AccessoriesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible.")

        # Verify main navigation links
        try:
            clothes_link = wait.until(EC.visibility_of_element_located((By.ID, "category-3")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.ID, "category-6")))
            art_link = wait.until(EC.visibility_of_element_located((By.ID, "category-9")))
        except:
            self.fail("Main navigation links are not visible.")

        # Verify login button
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='login']")))
        except:
            self.fail("Login button is not visible.")

        # Verify search bar
        try:
            search_bar = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search our catalog']")))
        except:
            self.fail("Search bar is not visible.")

        # Check product list
        try:
            products_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        except:
            self.fail("Product list is not visible.")

        # Check for each product in the list
        try:
            products = wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "product-miniature")))
            self.assertGreater(len(products), 0, "No products are visible in the product list.")
        except:
            self.fail("Products are not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()