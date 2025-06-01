import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver

        # Step 1: Open home page
        self.assertTrue(driver.title, "Failed to load homepage")

        # Step 2: Navigate to "Art" category
        art_category_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Art")))
        self.assertTrue(art_category_link.is_displayed(), "Art category link not found")
        art_category_link.click()

        # Step 3: Wait for the filter sidebar to be present
        filter_sidebar = self.wait.until(EC.presence_of_element_located((By.ID, "search_filters")))
        self.assertTrue(filter_sidebar.is_displayed(), "Filter sidebar not found")

        # Get initial product count
        initial_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        initial_count = len(initial_products)
        self.assertGreater(initial_count, 0, "No products found initially")

        # Step 4: Select the "Matt paper" filter by label
        filter_label = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Matt paper')]")))
        filter_label.click()

        # Step 5: Wait for the page to update and verify product count reduced
        WebDriverWait(driver, 20).until(EC.staleness_of(initial_products[0]))
        filtered_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        filtered_count = len(filtered_products)
        
        self.assertLess(filtered_count, initial_count, "Filter did not reduce product count")

        # Step 6: Click the "Clear all" button to remove filters
        clear_all_button = driver.find_element(By.XPATH, "//button[contains(text(),'OK')]")
        self.assertTrue(clear_all_button.is_displayed(), "Clear all filters button not found")
        clear_all_button.click()

        # Step 7: Verify product count returns to original
        WebDriverWait(driver, 20).until(EC.staleness_of(filtered_products[0]))
        final_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        final_count = len(final_products)

        self.assertEqual(final_count, initial_count, "Product count did not return to original after clearing filters")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()