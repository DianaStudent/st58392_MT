from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class TestSeleniumAutomation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)

    def test_search_and_filter_books_by_price(self):
        driver = self.driver

        # Step 1: Open the home page
        driver.get("http://max/")  # Replace with actual base URL

        # Step 2: Click on the "Search" link
        search_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        if not search_link:
            self.fail("Search link not found on the page.")
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        search_input = self.wait.until(EC.element_to_be_clickable((By.ID, "q")))
        if not search_input:
            self.fail("Search input field not found on the page.")
        search_input.send_keys("book")

        search_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.search-button")))
        if not search_button:
            self.fail("Search button not found on the page.")
        search_button.click()

        # Step 4: Wait for the search results to load
        products_grid = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid")))
        if not products_grid:
            self.fail("Product grid not found after performing a search.")

        # Step 5: Locate and interact with the price range slider
        # In a real scenario, the slider interaction will depend on the specific implementation, assume CSS has sliders
        price_slider = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "selected-price-range")))
        if not price_slider:
            self.fail("Price range slider not found.")
        min_price = driver.find_element(By.CSS_SELECTOR, ".selected-price-range .from")
        max_price = driver.find_element(By.CSS_SELECTOR, ".selected-price-range .to")
        
        # Simulate dragging slider (assuming they are draggable and accept Actions Chains)
        sliders = driver.find_elements(By.CSS_SELECTOR, ".slider-handle")
        if len(sliders) < 2:
            self.fail("Slider handlers not found to adjust the price range.")

        # Dummy actions to simulate drag-and-drop, follow correct slider library syntax instead in real world
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(sliders[0], -10, 0).perform()  # Move min slider
        action.drag_and_drop_by_offset(sliders[1], 10, 0).perform()  # Move max slider

        # Wait for the filtering to apply dynamically
        self.wait.until(EC.staleness_of(products_grid))
        products_grid = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.products-wrapper")))

        # Step 6: Confirm that the product grid updates after slider movement
        item_boxes = driver.find_elements(By.CLASS_NAME, "item-box")
        self.assertTrue(len(item_boxes) > 0, "No products found in the filtered results.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()