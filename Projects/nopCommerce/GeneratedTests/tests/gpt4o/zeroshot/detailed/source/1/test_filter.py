from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class ProductFilterTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.implicitly_wait(10)

    def test_product_filter(self):
        driver = self.driver
        
        # Step 1: Open the home page (already done in setUp)

        # Step 2: Click on the "Search" link
        search_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        search_field.send_keys("book")
        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='button-1 search-button']"))
        )
        search_button.click()

        # Step 4: Wait for the search results to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "products-container"))
        )

        # Step 5: Locate and interact with the price range slider
        # Using ActionChains to simulate slider
        price_slider_from = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='from'])[1]"))
        )
        price_slider_to = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='to'])[1]"))
        )
        
        # Adjust slider to set range from 0 to 25
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(price_slider_to, -50, 0).perform()

        # Wait for filtering to apply dynamically
        WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element((By.XPATH, "(//span[@class='to'])[1]"), "25")
        )

        # Step 6: Confirm that the product grid updates after slider movement
        products = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "item-box"))
        )
        
        self.assertGreater(len(products), 0, "Product grid did not update with filtered results.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()