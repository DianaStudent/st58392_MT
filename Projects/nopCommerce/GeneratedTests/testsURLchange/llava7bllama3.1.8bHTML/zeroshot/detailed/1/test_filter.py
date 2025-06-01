import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")

    def test_search_and_filter(self):
        # Click on the "Search" link
        search_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/search']"))
        )
        search_link.click()

        # Enter "book" in the search field and submit the search
        search_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "query"))
        )
        search_field.send_keys("book")
        search_submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        search_submit_button.click()

        # Wait for the search results to load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid"))
        )

        # Locate and interact with the price range slider:
        min_slider_handle = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='minPrice']"))
        )
        max_slider_handle = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='maxPrice']"))
        )

        # Adjust the minimum or maximum slider handle to set a specific range (e.g. 0–25).
        min_slider_handle.send_keys("0")
        max_slider_handle.send_keys("25")

        # Wait for the filtering to apply dynamically
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid"))
        )

        # Confirm that:
        # - The product grid updates after slider movement.
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, ".product-grid")), 0)

        # At least one product is shown in the filtered results
        self.assertNotEqual(0, len(self.driver.find_elements(By.XPATH, "//div[@class='product']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()