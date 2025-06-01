from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
    
    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open category page
        category_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Art")))
        category_link.click()

        # Wait for filter sidebar to be present
        filter_sidebar = wait.until(EC.presence_of_element_located((By.ID, "search_filters")))

        # Select the filter using label-based selection: Matt paper
        matt_paper_checkbox = filter_sidebar.find_element(By.XPATH, "//a[contains(text(), 'Matt paper')]")
        matt_paper_checkbox.click()

        # Wait for the page to update and verify that the number of visible product items is reduced
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".js-product")))
        reduced_items = len(driver.find_elements(By.CSS_SELECTOR, ".js-product"))
        if reduced_items >= 7:
            self.fail("Product count did not reduce after filter applied.")

        # Clear the filter
        clear_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ok')]")))
        clear_filter.click()

        # Verify that the number of products returns to the original count
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".js-product")))
        original_count = len(driver.find_elements(By.CSS_SELECTOR, ".js-product"))
        if original_count != 7:
            self.fail("Product count did not return to original after clearing filters.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()