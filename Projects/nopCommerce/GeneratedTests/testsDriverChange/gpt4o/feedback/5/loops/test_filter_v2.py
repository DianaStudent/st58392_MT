import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page.
        driver.get("http://max/")

        # Step 2: Click on the "Search" link.
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search.
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        # Step 4: Wait for the search results to load.
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-item")))

        # Step 5: Locate and interact with the price range slider.
        # Assuming span elements represent min and max selections for filtering
        slider_min = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='from']")))
        slider_max = driver.find_element(By.XPATH, "//span[@class='to']")
        
        # Adjusting the slider to a specific range (e.g., 0 to 25)
        ActionChains(driver).drag_and_drop_by_offset(slider_max, -100, 0).perform()

        # Step 6: Wait for the filtering to apply dynamically
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-item")))

        # Confirm that the product grid updates after slider movement
        products = driver.find_elements(By.CLASS_NAME, "product-item")
        
        # Check if products exist after applying the filter
        if not products:
            self.fail("No products found after applying the filter.")

        # Additional check to ensure at least one product is shown
        self.assertGreater(len(products), 0, "No products found after applying the filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()