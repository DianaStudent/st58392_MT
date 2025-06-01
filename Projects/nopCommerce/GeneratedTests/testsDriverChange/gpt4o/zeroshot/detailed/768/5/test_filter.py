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
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter_by_price(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page and click on the "Search" link.
        search_link = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='top-menu notmobile']//a[@href='/search']")))
        search_link.click()

        # Step 2: Enter "book" in the search field and submit the search.
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-button")))
        search_button.click()

        # Step 3: Wait for the search results to load.
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        # Step 4: Locate and adjust the price range slider.
        from_slider = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='selected-price-range']/span[@class='from']")))
        to_slider = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='selected-price-range']/span[@class='to']")))

        # Use ActionChains to interact with sliders (assuming sliders have specific class 'ui-slider-handle').
        from_slider_handle = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'ui-slider-handle')][1]")))
        to_slider_handle = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'ui-slider-handle')][2]")))

        # Step 5: Adjust the slider range
        actions = ActionChains(driver)
        # Assuming we need to drag the sliders by an offset (arbitrary values, may need adjusting based on actual slider functionality)
        actions.drag_and_drop_by_offset(from_slider_handle, 0, 0).perform()
        actions.drag_and_drop_by_offset(to_slider_handle, -100, 0).perform()

        # Step 6: Confirm that the product grid updates after slider movement.
        products_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-container")))
        products = products_container.find_elements(By.CLASS_NAME, "product-item")

        if not products:
            self.fail("No products found within the price range on filtering.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()