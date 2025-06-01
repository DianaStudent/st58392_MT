import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page (already done in setUp)

        # Step 2: Click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 3: Enter "book" in the search field and submit
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.search-box-button")))
        search_button.click()

        # Step 4: Wait for search results to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid")))

        # Step 5: Locate and interact with the price range slider
        slider_from = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.selected-price-range span.from")))
        slider_to = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.selected-price-range span.to")))

        # Assuming the slider handle has a specific class or identification logic
        slider_handle = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='ui-slider-handle'][1]"))
        )
        ActionChains(driver).drag_and_drop_by_offset(slider_handle, 100, 0).perform()  # Adjust as needed

        # Wait for the filtering to apply
        wait.until(lambda driver: "25" in driver.find_element(By.CSS_SELECTOR, "div.selected-price-range span.to").text)

        # Step 6: Confirm that the product grid updates after slider movement
        products = driver.find_elements(By.CSS_SELECTOR, "div.item-grid div.item-box")
        if not products:
            self.fail("No products found after applying filter")

        # Confirm that at least one product is shown in the filtered results
        self.assertGreater(len(products), 0, "Expected at least one product in the results")

if __name__ == "__main__":
    unittest.main()