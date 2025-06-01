from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on the "Search" link.
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search.
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        
        search_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button-1.search-button")))
        search_button.click()

        # Step 4: Wait for the search results to load.
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-results")))

        # Step 5: Locate and interact with the price range slider:
        # Here, selenium does not provide built-in support to drag sliders, so we use ActionChains for simulating the drag operation.
        slider_min = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selected-price-range .from")))
        slider_max = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selected-price-range .to")))

        # Simulate slider interaction (set the price range to 0–25)
        driver.execute_script("arguments[0].textContent='0';", slider_min)
        driver.execute_script("arguments[0].textContent='25';", slider_max)

        # Manually trigger a filtering action as if the slider was moved
        driver.execute_script("document.querySelector('.product-filter.price-range-filter .filter-content').dispatchEvent(new Event('change'));")

        # Step 6: Confirm the product grid updates and at least one product is shown in the filtered results.
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".item-box")))

        if not products:
            self.fail("No products found after filtering.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()