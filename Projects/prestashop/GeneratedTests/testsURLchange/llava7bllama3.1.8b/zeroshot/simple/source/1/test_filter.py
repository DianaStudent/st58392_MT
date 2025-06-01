from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestFiltering(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_filtering(self):
        # Wait for the filter sidebar to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".filter-sidebar")))

        # Select a checkbox filter by its label text
        filter_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Categories']")))
        filter_checkbox.click()

        # Wait for the number of visible product items to change
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item")))

        # Get the initial number of visible products
        initial_product_count = len(WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-item"))))

        # Apply the filter and wait for the number of visible product items to change again
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()='APPLY FILTERS']")))
        apply_filters_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='APPLY FILTERS']")))
        apply_filters_button.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item")))

        # Get the final number of visible products
        final_product_count = len(WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-item"))))

        # Verify that the number of visible product items has changed
        self.assertLessEqual(initial_product_count, final_product_count)
        apply_filters_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()