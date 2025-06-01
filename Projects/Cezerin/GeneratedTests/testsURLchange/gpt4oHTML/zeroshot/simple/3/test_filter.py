import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestFilterFunctionality(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/category-a')  # Adjust to the path of your local HTML file
        self.wait = WebDriverWait(self.driver, 20)

    def test_filters(self):
        driver = self.driver

        # Wait for the "Brand A" filter checkbox and click it
        try:
            brand_a_checkbox = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="attribute-title" and text()="Brand"]/following-sibling::label/input'))
            )
            brand_a_checkbox.click()
        except:
            self.fail("Brand A checkbox not found.")

        # Wait for products to filter and count them
        sleep(2)  # Sleep to ensure the UI has updated
        try:
            product_cards_after_filter = driver.find_elements(By.XPATH, '//div[@class="columns is-multiline is-mobile products"]/div')
            self.assertEqual(len(product_cards_after_filter), 1, "Product count after applying 'Brand A' filter is incorrect.")
        except:
            self.fail("Product elements not found after applying filter.")

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()

        # Assume interaction with price slider (here simply imagined since a UI component is not available in static HTML)
        try:
            price_min_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="price-filter-values"]/div[@class="column has-text-left"]'))
            )
            price_max_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="price-filter-values"]/div[@class="column has-text-right"]'))
            )
            # Dummy interaction simulating price change
            price_min_value = float(price_min_element.text.replace('$', '').replace(',', ''))
            price_max_value = float(price_max_element.text.replace('$', '').replace(',', ''))
            self.assertNotEqual(price_min_value, 950.00, "Price min did not change.")  # Fails if not imaginative logic
        except:
            self.fail("Price filter elements not found or unable to interact.")

        # Wait and count products again
        sleep(2)
        try:
            product_cards_after_unselect = driver.find_elements(By.XPATH, '//div[@class="columns is-multiline is-mobile products"]/div')
            self.assertEqual(len(product_cards_after_unselect), 2, "Product count after removing 'Brand A' filter is incorrect.")
        except:
            self.fail("Product elements not found after removing filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()