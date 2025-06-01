import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_product_filter(self):
        driver = self.driver

        # Navigate to Search page
        try:
            search_page_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//li/a[@href='/search']"))
            )
            search_page_link.click()
        except Exception as e:
            self.fail(f"Search page link not found: {str(e)}")

        # Search for "book"
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.send_keys("book")

            search_button = driver.find_element(By.CLASS_NAME, "search-button")
            search_button.click()
        except Exception as e:
            self.fail(f"Search input or button not found: {str(e)}")

        # Apply price filter by navigating directly to a URL
        try:
            driver.get("http://max/search?q=book&price=0-25")
        except Exception as e:
            self.fail(f"Failed to navigate to price filtered URL: {str(e)}")

        # Verify the product grid is updated
        try:
            product_grid = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
            self.assertIsNotNone(product_grid, "Product grid not updated")
        except Exception as e:
            self.fail(f"Product grid not found or not updated: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()