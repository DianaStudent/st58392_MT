import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Click on the "Search" link from the top navigation.
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except Exception as e:
            self.fail(f"Failed to click search link: {e}")

        # 2. Enter the search term and perform the search.
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.send_keys("book")
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Failed to enter search term and submit: {e}")

        # 3. Apply price filter directly via URL
        try:
            driver.get(self.base_url + "search?q=book")
            driver.get(self.base_url + "search?q=book&price=0-25")
        except Exception as e:
            self.fail(f"Failed to navigate to filtered URL: {e}")

        # 4. Verify the product list is changed
        try:
            product_grid = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
            items = product_grid.find_elements(By.CLASS_NAME, "item-box")
            if not items:
                self.fail("No items found in the product grid after filtering.")
            prices = []
            for item in items:
                try:
                    price_element = item.find_element(By.CLASS_NAME, "price.actual-price")
                    price_text = price_element.text.replace('$', '')
                    price = float(price_text)
                    prices.append(price)
                except:
                    pass

            for price in prices:
                if price > 25:
                    self.fail("Product with price greater than 25 found after filtering.")
        except Exception as e:
            self.fail(f"Failed to verify product list: {e}")

if __name__ == "__main__":
    unittest.main()