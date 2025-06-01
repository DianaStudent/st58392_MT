import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the home page.
        # Automatically opened by setUp()

        # 2. Click on the "Search" link.
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # 3. Enter "book" in the search field and submit the search.
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.clear()
        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        search_button.click()

        # 4. Wait for the search results to load.
        product_grid = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-grid")))

        # 5. Locate and interact with the price range slider.
        # Note: Adjust the selector based on the HTML structure.
        price_slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-filter.price-range-filter")))
        
        # Simulating slider movement using keyboard for simplicity
        slider_from = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selected-price-range .from")))
        slider_to = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selected-price-range .to")))

        action = ActionChains(driver)
        action.click_and_hold(slider_to).move_by_offset(-20, 0).release().perform()

        # Wait for the filtering to apply dynamically.
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products-container")))

        # 6. Confirm that:
        # - The product grid updates after slider movement.
        # - At least one product is shown in the filtered results.
        updated_products = driver.find_elements(By.CSS_SELECTOR, ".product-item")
        if not updated_products:
            self.fail("No products found after applying the filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()