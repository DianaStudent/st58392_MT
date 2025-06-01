from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestFilterSidebar(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")  # replace with your home page URL

    def test_filter_sidebar(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Categories']")))
        categories_link = self.driver.find_element(By.XPATH, "//a[text()='Categories']")
        categories_link.click()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "filter-sidebar")))

        # Select a checkbox filter
        filters_section = self.driver.find_element(By.CSS_SELECTOR, "[data-name='Product Category']")  # replace with actual section data-name value
        filters = filters_section.find_elements(By.XPATH, ".//label")
        for filter in filters:
            if filter.text == "Vector graphics":
                filter.click()
                break

        # Verify that the number of visible product items is reduced
        initial_products_count = len(self.driver.find_elements(By.CSS_SELECTOR, "[data-name='product-item']"))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "filter-sidebar")))
        applied_filter_label = self.driver.find_element(By.XPATH, "//label[@class='active']")
        if applied_filter_label.text != "Vector graphics":
            self.fail("Applied filter label does not match expected value")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "filter-sidebar")))
        new_products_count = len(self.driver.find_elements(By.CSS_SELECTOR, "[data-name='product-item']"))
        if new_products_count == initial_products_count:
            self.fail("Number of visible product items did not change after applying filter")

        # Clear all filters
        clear_all_button = self.driver.find_element(By.XPATH, "//button[text()='Clear all']")
        clear_all_button.click()

        # Verify that the number of products returns to the original count
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "filter-sidebar")))
        new_products_count_after_clearing = len(self.driver.find_elements(By.CSS_SELECTOR, "[data-name='product-item']"))
        if new_products_count_after_clearing != initial_products_count:
            self.fail("Number of products did not return to original count after clearing filters")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()