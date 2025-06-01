import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_product_filter(self):
        # Step 1: Open the home page
        self.driver.get("http://max/")

        # Step 2: Click on the "Search" link
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#q')))
        search_field.send_keys("book")
        search_button = self.driver.find_element(By.CSS_SELECTOR, 'button.search-button')
        search_button.click()

        # Step 4: Wait for the search results to load
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.products-container')))

        # Step 5: Locate and interact with the price range slider
        # Adjust the minimum slider handle to set a specific range, e.g., 0–25
        slider_from = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.product-filter.price-range-filter div.selected-price-range span.from')
        ))

        actions = ActionChains(self.driver)
        actions.click_and_hold(slider_from).move_by_offset(20, 0).release().perform()

        # Wait for the filtering to apply dynamically
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.product-item')))

        # Step 6: Confirm that the product grid updates after slider movement
        # At least one product is shown in the filtered results
        products = self.driver.find_elements(By.CSS_SELECTOR, 'div.product-item')
        
        if len(products) == 0:
            self.fail("No products found after filtering.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()