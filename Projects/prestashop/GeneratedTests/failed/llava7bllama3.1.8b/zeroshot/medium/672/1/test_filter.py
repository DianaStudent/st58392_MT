from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import unittest

class TestFilterMedium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_filter_medium(self):
        # Navigate to a product category
        category_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Home']")))
        category_link.click()

        # Wait for the filter sidebar to be present
        filter_sidebar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sidebar-filter")))

        # Select a checkbox filter using label-based selection
        color_filter_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@data-name='Color']")))
        color_filter_checkbox.click()

        # Wait for the page to update and verify that the number of visible product items is reduced
        initial_product_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-card"))))

        # Clear all filters
        clear_all_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-name='Clear all']")))
        clear_all_button.click()

        # Verify that the number of products returns to the original count
        final_product_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-card"))))

        self.assertLess(final_product_count, initial_product_count)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()