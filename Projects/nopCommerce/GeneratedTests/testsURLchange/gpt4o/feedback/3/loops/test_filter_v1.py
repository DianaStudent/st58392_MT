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
        self.driver.maximize_window()
        self.driver.get("http://max/")
    
    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page
        try:
            home_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.top-menu.notmobile li a[href='/']")))
        except Exception:
            self.fail("Home page did not load properly.")

        # Step 2: Click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.top-menu.notmobile li a[href='/search']")))
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        search_input.send_keys('book')
        search_button.click()

        # Step 4: Wait for the search results to load
        try:
            results_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.products-container")))
        except Exception:
            self.fail("Search results did not load.")

        # Step 5: Locate and interact with the price range slider
        price_range_from = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.selected-price-range span.from")))
        price_range_to = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.selected-price-range span.to")))

        # Use ActionChains to drag the slider handles
        try:
            slider_handle_min = driver.find_element(By.CSS_SELECTOR, ".noUi-handle-lower")
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(slider_handle_min, 50, 0).perform()  # This value may need adjustment
        except Exception:
            self.fail("Could not interact with the price range slider.")

        # Wait for filtering to apply
        WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.selected-price-range span.to"), '25')
        )

        # Step 6: Confirm the results
        filtered_result_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.products-wrapper div.item-box")))
        if not filtered_result_items:
            self.fail("No products found within the specified price range.")
        
        print(f"Number of items in the filtered result: {len(filtered_result_items)}")
        self.assertTrue(len(filtered_result_items) > 0)

if __name__ == "__main__":
    unittest.main()