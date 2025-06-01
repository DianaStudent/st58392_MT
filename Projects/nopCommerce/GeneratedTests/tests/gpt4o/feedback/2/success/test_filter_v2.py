from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open home page
        home_page_selector = (By.XPATH, "//li/a[contains(text(),'Home page')]")
        wait.until(EC.presence_of_element_located(home_page_selector))

        # Step 2: Click the "Search" link
        search_link_selector = (By.XPATH, "//a[contains(text(),'Search')]")
        search_link = wait.until(EC.element_to_be_clickable(search_link_selector))
        search_link.click()

        # Step 3: Enter "book" in the search field and submit
        search_field_selector = (By.ID, "q")
        search_field = wait.until(EC.presence_of_element_located(search_field_selector))
        search_field.clear()
        search_field.send_keys("book")
        
        search_button_selector = (By.CLASS_NAME, "search-button")
        search_button = wait.until(EC.element_to_be_clickable(search_button_selector))
        search_button.click()

        # Step 4: Wait for search results to load
        results_selector = (By.CLASS_NAME, "products-container")
        wait.until(EC.presence_of_element_located(results_selector))

        # Step 5: Locate and interact with the price range slider
        from_slider_selector = (By.XPATH, "//div[@class='product-filter price-range-filter']//span[@class='from']")
        to_slider_selector = (By.XPATH, "//div[@class='product-filter price-range-filter']//span[@class='to']")
        from_slider = wait.until(EC.presence_of_element_located(from_slider_selector))
        to_slider = wait.until(EC.presence_of_element_located(to_slider_selector))
        
        # Adjust the slider using ActionChains
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(from_slider, 15, 0).perform()
        actions.drag_and_drop_by_offset(to_slider, -25, 0).perform()

        # Wait for filtering to apply dynamically by waiting for changes in the product grid
        new_results_selector = (By.CLASS_NAME, "item-box")
        filtered_products = wait.until(EC.presence_of_all_elements_located(new_results_selector))
        
        if not filtered_products:
            self.fail("No products displayed after applying the filter.")
        
        # Step 7: Confirm at least one product is shown in the filtered results
        self.assertGreater(len(filtered_products), 0, "No products found after filter applied.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()