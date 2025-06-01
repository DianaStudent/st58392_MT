import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProductFilter(unittest.TestCase):
    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")  # Set this to the correct URL

    def test_filter_products(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Wait for and click on the tab for filtering "Tables"
            tables_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.product-tab-list a[data-rb-event-key="tables"]')))
            tables_count = len(driver.find_elements(By.CSS_SELECTOR, '.tab-content .tab-pane.show .product-wrap-2'))
            tables_tab.click()
            
            # Wait for products to be filtered and check the result
            wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, '.tab-content .tab-pane.active.show .product-wrap-2')) != tables_count)

            # Ensure at least one product is displayed
            filtered_count = len(driver.find_elements(By.CSS_SELECTOR, '.tab-content .tab-pane.active.show .product-wrap-2'))
            self.assertGreater(filtered_count, 0, "Product count did not change after applying filter")

        except Exception as e:
            self.fail(f"Test failed due to an exception: {str(e)}")

    def tearDown(self):
        # Teardown the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()