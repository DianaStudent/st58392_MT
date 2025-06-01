import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class FilterTest(unittest.TestCase):
    def setUp(self):
        # Set up ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")  # Navigate to Art category page

    def tearDown(self):
        # Tear down the driver
        self.driver.quit()

    def test_filter_composition(self):
        driver = self.driver
        
        # Wait for the filter sidebar to be present
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div#search_filters"))
            )
        except Exception as e:
            self.fail("Filter sidebar not found: " + str(e))

        # Locate the product list and get the initial count of visible products
        try:
            initial_products = driver.find_elements(By.CSS_SELECTOR, "div.js-product.product")
            initial_count = len(initial_products)
        except Exception as e:
            self.fail("Could not count initial products: " + str(e))
        
        # Apply the filter by checking the checkbox for 'Matt paper'
        try:
            matt_paper_filter_label = driver.find_element(By.XPATH, "//a/span[text()='Matt paper']")
            matt_paper_filter = matt_paper_filter_label.find_element(By.XPATH, "..//preceding-sibling::span/input")
            matt_paper_filter.click()
        except Exception as e:
            self.fail("Could not find or click the 'Matt paper' filter: " + str(e))

        # Wait for the product list to refresh
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.js-product.product"))
        )

        # Get the count of visible products after applying the filter
        try:
            filtered_products = driver.find_elements(By.CSS_SELECTOR, "div.js-product.product")
            filtered_count = len(filtered_products)
        except Exception as e:
            self.fail("Could not count filtered products: " + str(e))

        # Ensure the count of products has changed
        self.assertNotEqual(initial_count, filtered_count, "Product count did not change after applying filter")

        # Uncheck the filter to clear it
        try:
            matt_paper_filter.click()
        except Exception as e:
            self.fail("Could not uncheck the 'Matt paper' filter: " + str(e))

        # Wait for the product list to refresh
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.js-product.product"))
        )

        # Get the count of visible products after clearing the filter
        try:
            final_products = driver.find_elements(By.CSS_SELECTOR, "div.js-product.product")
            final_count = len(final_products)
        except Exception as e:
            self.fail("Could not count products after clearing the filter: " + str(e))

        # Ensure the count returns to the initial number
        self.assertEqual(initial_count, final_count, "Product count did not revert back after clearing filter")


if __name__ == "__main__":
    unittest.main()