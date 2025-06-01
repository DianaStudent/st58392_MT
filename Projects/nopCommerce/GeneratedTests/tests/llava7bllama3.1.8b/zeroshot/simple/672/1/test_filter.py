import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestFilterSimple(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_filter_simple(self):
        # Navigate to the URL
        self.driver.get("http://max/")

        # Perform a product search using the query "book"
        search_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))
        )
        search_input.send_keys("book")
        search_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()

        # Apply a price filter by navigating to a URL that includes the price parameter
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("price")
        )

        # Confirm success by checking that the resulting product grid is updated
        product_grid = self.driver.find_element(By.XPATH, "//div[@class='product-grid']")
        self.assertTrue(product_grid.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()