from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_filter_products(self):
        # Navigate to a product category
        self.driver.find_element(By.XPATH, "//a[@href='/home-accessories']").click()

        # Wait for the filter sidebar to be present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "filter-sidebar")))

        # Select a checkbox filter by label text
        checkboxes = self.driver.find_elements(By.XPATH, "//label[@class='form-check-label']")
        checkbox = [c for c in checkboxes if 'Brown bear' in c.text][0]
        checkbox.click()

        # Wait for the page to update and verify that the number of visible product items is reduced
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='row']")))
        original_product_count = len(self.driver.find_elements(By.XPATH, "//div[@class='col-md-4']"))
        self.assertLess(len(self.driver.find_elements(By.XPATH, "//div[@class='col-md-4']")), original_product_count)

        # Click the "Clear all" button to remove filters
        self.driver.find_element(By.XPATH, "//button[@data-name='clear-all']").click()

        # Verify that the number of products returns to the original count
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='row']")))
        current_product_count = len(self.driver.find_elements(By.XPATH, "//div[@class='col-md-4']"))
        self.assertEqual(current_product_count, original_product_count)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()