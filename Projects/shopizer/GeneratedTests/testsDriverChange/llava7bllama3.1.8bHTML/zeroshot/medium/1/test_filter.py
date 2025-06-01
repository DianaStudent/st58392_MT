import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFilters(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_filters(self):
        self.driver.get("http://localhost/")  # assuming this is the url of your webpage

        # Click on "Tables" tab to filter products
        tables_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Tables"))
        )
        tables_tab.click()

        # Verify that at least one product appears
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-card"))
        ))

        # Click on the "Chairs" tab to change the filter
        chairs_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Chairs"))
        )
        chairs_tab.click()

        # Verify that product list is updated
        old_product_count = len(WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".product-card")
        )))

        # Click on the "All" tab to remove the filter
        all_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "All"))
        )
        all_tab.click()

        # Verify that full list of products is shown and product count changes
        new_product_count = len(WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".product-card")
        )))

        self.assertNotEqual(old_product_count, new_product_count)
        self.assertTrue(new_product_count > old_product_count)

if __name__ == "__main__":
    unittest.main()