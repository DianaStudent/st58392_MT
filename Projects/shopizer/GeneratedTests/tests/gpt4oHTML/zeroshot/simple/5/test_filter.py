import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class FilterProductTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.get("http://localhost:8080")  # Adjust with the actual URL where the HTML content is hosted

    def setUp(self):
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_tables(self):
        # Click on the Tables filter tab
        try:
            tables_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']")))
            tables_tab.click()
        except Exception as e:
            self.fail(f"Tables filter tab not found or clickable: {e}")

        # Wait for the content under the 'tables' filter to appear
        try:
            tables_content = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-rb-event-key='tables']//div[contains(@class, 'product-wrap-2')]")))
            product_count = len(self.driver.find_elements(By.XPATH, "//div[@data-rb-event-key='tables']//div[contains(@class, 'product-wrap-2')]"))
            self.assertGreater(product_count, 0, "No products displayed for 'Tables' filter.")
        except Exception as e:
            self.fail(f"No products found after filtering for Tables: {e}")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()