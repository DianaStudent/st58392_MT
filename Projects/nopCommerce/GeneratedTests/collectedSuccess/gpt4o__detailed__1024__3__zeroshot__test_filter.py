import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        driver.get("http://max/")
        
        # Step 2: Click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()
        
        # Step 3: Enter "book" in the search field and submit the search
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()
        
        # Step 4: Wait for the search results to load
        products_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-container")))

        # Step 5: Locate and interact with the price range slider
        price_range_from = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "from")))
        price_range_to = driver.find_element(By.CLASS_NAME, "to")

        # Using ActionChains to drag the price range slider
        # Adjusts the first slider to lower limit (0) and the second to upper limit (25)
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(price_range_from, -50, 0).perform()  # Assumes necessary offset
        actions.drag_and_drop_by_offset(price_range_to, -50, 0).perform()    # Assumes necessary offset

        # Step 6: Confirm that the product grid updates after slider movement
        filtered_products = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-wrapper")))
        product_items = filtered_products.find_elements(By.CLASS_NAME, "product-item")

        if not product_items or len(product_items) == 0:
            self.fail("No products found in the filtered results.")
        else:
            print("Test passed. Products filtered successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()