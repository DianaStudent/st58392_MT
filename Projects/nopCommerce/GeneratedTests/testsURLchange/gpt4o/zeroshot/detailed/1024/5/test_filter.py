import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        # 1. Open the home page.
        self.driver.get("http://max/")

        # 2. Click on the "Search" link.
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # 3. Enter "book" in the search field and submit the search.
        search_field = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_field.send_keys("book")
        search_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-button")))
        search_button.click()

        # 4. Wait for the search results to load.
        results = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        # Check if search results exist and are not empty
        self.assertTrue(results, "Search results did not load.")

        # 5. Locate and interact with the price range slider
        # Assuming slider interaction requires adjusting a handle
        slider = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "selected-price-range")))
        actions = ActionChains(self.driver)

        # Adjust the maximum slider handle
        max_slider_handle = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='to']")))
        
        # Click and drag the slider handle (adjusting simulation with keys)
        actions.click_and_hold(max_slider_handle).send_keys(Keys.ARROW_LEFT).perform()

        # Wait for filter to apply
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-container")))

        # 6. Confirm that at least one product is shown in the filtered results
        filtered_results = self.driver.find_elements(By.CLASS_NAME, "item-box")
        if not filtered_results:
            self.fail("No products are shown in the filtered results.")
        
        self.assertTrue(len(filtered_results) > 0, "Filtered results show no products.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()