import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductFilter(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_product_filter(self):
        driver = self.driver
        wait = self.wait
        
        # Navigate to Search
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        self.assertIsNotNone(search_link, "Search link not found")
        search_link.click()
        
        # Enter search keyword and submit
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        self.assertIsNotNone(search_input, "Search input not found")
        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, ".button-1.search-button")
        search_button.click()
        
        # Wait for search results to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products-container")))
        
        # Adjust price range slider
        # Slider elements are assumed here to be part of a range input. Adjust as needed if another method is used.
        min_slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selected-price-range .from")))
        max_slider = driver.find_element(By.CSS_SELECTOR, ".selected-price-range .to")
        self.assertIsNotNone(min_slider, "Min slider not found")
        self.assertIsNotNone(max_slider, "Max slider not found")
        
        actions = ActionChains(driver)
        # For demonstration, assuming sliders can be moved with offset
        # This section might need adjustment to match the slider's actual interaction model
        actions.click_and_hold(min_slider).move_by_offset(0, 0).release().perform()
        actions.click_and_hold(max_slider).move_by_offset(-25, 0).release().perform()

        # Wait for the filter to apply
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products-container .item-box")))

        # Verify filtered results
        items = driver.find_elements(By.CSS_SELECTOR, ".products-container .item-box")
        self.assertGreater(len(items), 0, "No products found after applying the filter")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()