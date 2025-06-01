import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver

        # 1. Open the home page
        # Already achieved in setUp with driver.get

        # 2. Click on the "Search" link
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # 3. Enter "book" in the search field and submit the search.
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        submit_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.search-button")))
        
        search_box.send_keys("book")
        submit_button.click()

        # 4. Wait for the search results to load.
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-container")))

        # 5. Locate and interact with the price range slider.
        # Assume the slider elements and interactions need to be adjusted for specific implementation.
        
        price_range_from = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "selected-price-range")))

        # Interact with the slider handles to set the price range
        slider = driver.find_element(By.CLASS_NAME, "selected-price-range")
        # Here we need to use ActionChains to drag the slider, adjust according to your own slider script
        
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(slider, -30, 0).perform()  # Adjust arguments as needed

        # 6. Confirm that:
        # - The product grid updates after slider movement.
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "item-grid")))

        # - At least one product is shown in the filtered results
        items = driver.find_elements(By.CLASS_NAME, "item-box")
        if not items or len(items) == 0:
            self.fail("No products found after filtering!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()