import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


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
        except NoSuchElementException:
            self.fail("Search link not found")

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
        except NoSuchElementException:
            self.fail("Search input or button not found")

        # 3. Verify search results are displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
            )
        except NoSuchElementException:
            self.fail("Search results not found")

        # 4. Apply price filter by navigating to a URL that includes the price parameter.
        driver.get(self.base_url + "search?q=book")
        driver.execute_script("window.location.href = '/search?q=book&price=0-25'")
        WebDriverWait(driver, 20).until(EC.url_contains("price=0-25"))

        # 5. Confirm success by checking that the resulting product grid is updated.
        try:
            product_grid = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
            self.assertTrue(product_grid.is_displayed(), "Product grid is not displayed after filtering.")
        except NoSuchElementException:
            self.fail("Product grid not found")

        # 6. Check if the product list is changed
        product_items = driver.find_elements(By.CLASS_NAME, "product-item")
        self.assertTrue(len(product_items) > 0, "No products found after filtering.")

        # Verify that each product's price is within the filter range (0-25)
        for product_item in product_items:
            try:
                price_element = product_item.find_element(By.CLASS_NAME, "actual-price")
                price_text = price_element.text
                if price_text:
                    price = float(price_text.replace("$", ""))
                    self.assertTrue(0 <= price <= 25, f"Product price {price} is not within the range 0-25.")
            except NoSuchElementException:
                print("Price element not found for a product. Skipping price check.")


if __name__ == "__main__":
    unittest.main()