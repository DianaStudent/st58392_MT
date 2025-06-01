from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on the "Search" link
        search_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.top-menu.notmobile a[href="/search"]')))
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_field = wait.until(EC.element_to_be_clickable((By.ID, 'q')))
        search_field.send_keys("book")

        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-1.search-button')))
        search_button.click()

        # Step 4: Wait for the search results to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.products-container')))

        # Step 5: Locate and interact with the price range slider to set a specific range (e.g. 0–25)
        from_slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.selected-price-range .from')))
from selenium.webdriver.chrome.service import Service as ChromeService
        to_slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.selected-price-range .to')))

        # Use ActionChains to drag the sliders as required
        actions = ActionChains(driver)
        actions.click_and_hold(from_slider).move_by_offset(25, 0).release().perform()
        actions.click_and_hold(to_slider).move_by_offset(-25, 0).release().perform()

        # Step 6: Wait for filtering to apply dynamically and confirm the product grid updates
        products = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.products-wrapper .product-item')))
        
        # Confirm that at least one product is shown in the filtered results
        if not products.is_displayed():
            self.fail("No products displayed after applying filter")

if __name__ == "__main__":
    unittest.main()