import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        driver.get("http://max/")
        
        # Step 2: Click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_box = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_box.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "button-1.search-button")
        search_button.click()

        # Step 4: Wait for the search results to load
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))

        # Step 5: Locate and interact with the price range slider
        # Assuming the slider can be interacted by moving its handles via offset
        price_filter = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "price-range-filter")))
        from_slider = price_filter.find_element(By.XPATH, ".//input[@class='from']")
        to_slider = price_filter.find_element(By.XPATH, ".//input[@class='to']")
        
        # Create an action chain to slide the sliders
        actions = ActionChains(driver)
        actions.click_and_hold(from_slider).move_by_offset(10, 0).release().perform()  # Adjust offsets as needed
        actions.click_and_hold(to_slider).move_by_offset(-40, 0).release().perform()  # Adjust offsets as needed
        
        # Step 6: Confirm that the product grid updates after slider movement
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item")))

        # Check that at least one product is shown
        products = driver.find_elements(By.CLASS_NAME, "product-item")
        if not products:
            self.fail("No products found after applying price filter.")
    
if __name__ == "__main__":
    unittest.main()