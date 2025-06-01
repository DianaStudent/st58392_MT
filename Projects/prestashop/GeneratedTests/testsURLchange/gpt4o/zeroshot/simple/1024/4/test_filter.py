import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestProductFilter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the Art category
        art_category_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
        )
        art_category_link.click()

        # Wait for the filter sidebar
        filter_sidebar = wait.until(
            EC.presence_of_element_located((By.ID, "search_filters"))
        )

        # Select 'Matt paper' filter
        filter_label = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[contains(., 'Matt paper')]")
            )
        )
        filter_label.click()

        # Count products after applying the filter
        products_after_filter = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-miniature"))
        )
        count_after_filter = len(products_after_filter)

        # Verify product count changes after filter
        self.assertNotEqual(count_after_filter, 7, "Filter did not change the product count.")

        # Clear the filter by refreshing the page or using clear method if available
        driver.refresh()

        # Count products after clearing the filter
        products_after_clear = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-miniature"))
        )
        count_after_clear = len(products_after_clear)

        # Verify product count goes back to original
        self.assertEqual(count_after_clear, 7, "Product count did not revert back after clearing filter.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()