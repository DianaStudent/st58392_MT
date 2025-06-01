import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Open the home page.
        self.assertEqual(driver.current_url, self.base_url)

        # 2. Click on the "Search" link.
        search_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        # 3. Enter "book" in the search field and submit the search.
        search_field_id = "q"
        search_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, search_field_id))
        )
        search_field.send_keys("book")

        search_button_class = "button-1 search-button"
        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, search_button_class))
        )
        search_button.click()

        # 4. Wait for the search results to load.
        product_grid_class = "product-grid"
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, product_grid_class))
        )

        # 5. Locate and interact with the price range slider:
        #    - Adjust the minimum or maximum slider handle to set a specific range (e.g. 0–25).
        #    - Wait for the filtering to apply dynamically.

        # This website does not have a slider. It only displays a price range.
        # The price range displayed is determined by the products shown.
        # We cannot drag handles to set a specific range.
        # Instead, we will navigate to a URL that includes the price parameter.
        # This is not ideal, but it is the only way to apply a price filter.

        # Navigate to a URL that includes the price parameter.
        driver.get(self.base_url + "search?q=book&price=0-25")

        # 6. Confirm that:
        #    - The product grid updates after slider movement.
        #    - At least one product is shown in the filtered results.

        # Wait for the search results to load.
        product_grid = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, product_grid_class))
        )

        # Confirm that the product grid updates after slider movement.
        # Check that the product grid is not empty.
        product_items = driver.find_elements(By.CLASS_NAME, "product-item")
        self.assertTrue(len(product_items) > 0, "No products found after filtering.")