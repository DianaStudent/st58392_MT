import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("http://max/")

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page and click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 2: Enter "book" in the search field and submit the search
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.clear()
        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, '.button-1.search-button')
        search_button.click()

        # Step 3: Wait for the search results to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.products-container')))

        # Step 4: Locate and interact with the price range filter
        # We'll simulate dragging a slider to adjust the price range
        price_filter_min = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.selected-price-range .from')))
        price_filter_max = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.selected-price-range .to')))
        
        # Check the initial price range
        self.assertIsNotNone(price_filter_min.text)
        self.assertIsNotNone(price_filter_max.text)

        # Find the slider handles and drag them (mocked as manual actions due to HTML constraints)
        # You might want to fine-tune these operations based on the real slider implementation
        try:
            # Adjust the minimum slider to 0 and maximum to 25
            actions = ActionChains(driver)
            min_slider_handle = driver.find_element(By.CSS_SELECTOR, 'div.price-range-filter .from')
            actions.click_and_hold(min_slider_handle).move_by_offset(-30, 0).release().perform()

            max_slider_handle = driver.find_element(By.CSS_SELECTOR, 'div.price-range-filter .to')
            actions.click_and_hold(max_slider_handle).move_by_offset(-30, 0).release().perform()
        except Exception as e:
            self.fail(f"Failed to interact with sliders: {str(e)}")

        # Wait for the filtering to apply dynamically
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.selected-price-range .to'), "25"))

        # Step 5: Confirm the product grid updates after slider movement
        products_grid = driver.find_element(By.CSS_SELECTOR, '.products-grid')
        products = products_grid.find_elements(By.CSS_SELECTOR, '.item-box')
        self.assertGreater(len(products), 0, "No products found in the filtered results")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()