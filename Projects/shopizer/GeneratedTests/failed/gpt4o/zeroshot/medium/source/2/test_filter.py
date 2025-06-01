from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filters(self):
        driver = self.driver
        wait = self.wait
        
        # Accept cookies
        cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        cookie_button.click()

        # Verify home page loads
        self.assertTrue(driver.find_element(By.LINK_TEXT, "Home").is_displayed(), "Home link not found")

        # Click on the "Tables" tab
        tables_tab = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Tables")))
        tables_tab.click()

        # Verify at least one table product appears
        tables_products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active .product-wrap-2")))
        self.assertGreater(len(tables_products), 0, "No products found after selecting Tables filter")

        # Click on the "Chairs" tab
        chairs_tab = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Chairs")))
        chairs_tab.click()

        # Verify at least one chair product appears and list is updated
        chairs_products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active .product-wrap-2")))
        self.assertGreater(len(chairs_products), 0, "No products found after selecting Chairs filter")

        # Click on the "All" tab
        all_tab = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "All")))
        all_tab.click()

        # Confirm that the full list of products is shown
        all_products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active .product-wrap-2")))
        self.assertGreater(len(all_products), len(chairs_products), "Full list of products not shown after selecting All filter")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()