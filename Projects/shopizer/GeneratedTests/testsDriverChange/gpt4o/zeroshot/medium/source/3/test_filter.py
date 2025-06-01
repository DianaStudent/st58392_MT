import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept Cookies
        cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        cookie_button.click()

        # Select the "Tables" tab
        tables_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Tables')]")))
        tables_tab.click()

        # Verify at least one product is visible when filtered by "Tables"
        tables_products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[class='product-wrap-2']")))
        if not tables_products:
            self.fail("No products found for 'Tables' filter.")

        # Click on the "Chairs" tab
        chairs_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Chairs')]")))
        chairs_tab.click()

        # Verify products displayed have changed
        chairs_products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[class='product-wrap-2']")))
        if not chairs_products or len(chairs_products) == len(tables_products):
            self.fail("Product list did not change when 'Chairs' filter was applied.")

        # Click on "All" to show all products
        all_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'All')]")))
        all_tab.click()

        # Verify the full list of products is shown
        all_products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[class='product-wrap-2']")))
        if not all_products or len(all_products) <= len(chairs_products):
            self.fail("Full product list not shown after removing filters.")

if __name__ == "__main__":
    unittest.main()