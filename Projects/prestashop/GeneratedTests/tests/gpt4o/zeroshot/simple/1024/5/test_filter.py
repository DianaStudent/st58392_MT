import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_filter_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to 'Art' category
        art_category_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        art_category_link.click()

        # Verify the filter sidebar presence
        filter_sidebar = wait.until(EC.presence_of_element_located((By.ID, "search_filters")))
        if not filter_sidebar:
            self.fail("Filter sidebar is not present.")

        # Apply 'Composition - Matt paper' filter
        filter_label = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(., 'Matt paper')]")))
        filter_checkbox = filter_label.find_element(By.TAG_NAME, "input")
        filter_checkbox.click()

        # Wait for products to be filtered and count the results
        product_list = wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))
        filtered_products = product_list.find_elements(By.CLASS_NAME, "js-product")
        filtered_count = len(filtered_products)

        # Check product count after filter is applied
        self.assertNotEqual(filtered_count, 7, "Product count did not change after applying filter.")

        # Clear the filter
        filter_checkbox.click()

        # Wait for products to revert and count the results again
        reverted_products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "js-product")))
        reverted_count = len(reverted_products)

        # Verify product count changes back to original after filter removed
        self.assertEqual(reverted_count, 7, "Product count did not revert after removing filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()