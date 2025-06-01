import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Search']")))
        search_link.click()

        # Step 2: Enter "book" in the search field and submit
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.search-button")))
        submit_button.click()

        # Step 3: Wait for results to load and interact with price range slider
        price_from = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selected-price-range .from")))
        self.assertTrue(price_from, "Price range slider not found.")
        price_to = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selected-price-range .to")))
        self.assertTrue(price_to, "Price range slider not found.")

        # Using ActionChains to adjust the slider (Assuming slider handles are identifiable)
        slider = driver.find_element(By.CSS_SELECTOR, ".product-filter.price-range-filter .filter-content")
        ActionChains(driver).click_and_hold(slider).move_by_offset(-50, 0).release().perform()

        # Step 4: Check if product grid updates
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products-container .product-item")))
        product_items = driver.find_elements(By.CSS_SELECTOR, ".products-container .product-item")
        
        self.assertGreater(len(product_items), 0, "No products found after applying filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()