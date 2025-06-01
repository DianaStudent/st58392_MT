import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 2: Enter "book" in the search field and submit the search
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        
        search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-button")))
        search_button.click()

        # Step 3: Wait for the search results to load
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-wrapper")))
        if not product_grid:
            self.fail("Search results did not load.")

        # Step 4: Locate and interact with the price range slider
        price_from = driver.find_element(By.CSS_SELECTOR, ".selected-price-range .from")
        price_to = driver.find_element(By.CSS_SELECTOR, ".selected-price-range .to")
        if not price_from or not price_to:
            self.fail("Price range slider not found.")

        slider_bar = driver.find_element(By.CLASS_NAME, "price-range-filter")
        action = ActionChains(driver)
        # Adjust the sliders; Here we simulate dragging with an offset
        action.click_and_hold(slider_bar).move_by_offset(-50, 0).release().perform()  # Adjust this offsets
        action.click_and_hold(slider_bar).move_by_offset(50, 0).release().perform()  # Adjust this offsets

        # Step 5: Confirm the product grid updates and product is shown
        filtered_results = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-wrapper")))
        if not filtered_results:
            self.fail("Product grid did not update after slider adjustment.")

        items = driver.find_elements(By.CLASS_NAME, "item-box")
        if not items:
            self.fail("No products found after applying filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()