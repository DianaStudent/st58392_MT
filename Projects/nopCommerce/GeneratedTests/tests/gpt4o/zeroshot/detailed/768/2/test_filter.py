import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_box = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_box.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        # Step 4: Wait for the search results to load
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))

        # Step 5: Locate and interact with the price range slider
        try:
            price_range_filter = driver.find_element(By.CLASS_NAME, "price-range-filter")
            slider_from = price_range_filter.find_element(By.CLASS_NAME, "from")
            slider_to = price_range_filter.find_element(By.CLASS_NAME, "to")

            # Example slider interaction (adjust as per UI behavior)
            # Drag the "to" slider
            actions = ActionChains(driver)
            actions.click_and_hold(slider_to).move_by_offset(-50, 0).release().perform()

            # Wait for filtering to apply dynamically and check the grid updates
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))
        except Exception as e:
            self.fail(f"Slider interaction failed: {e}")

        # Step 6: Confirm that at least one product is shown in the filtered results
        products = driver.find_elements(By.CLASS_NAME, "product-item")
        if not products:
            self.fail("No products found after applying price filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()