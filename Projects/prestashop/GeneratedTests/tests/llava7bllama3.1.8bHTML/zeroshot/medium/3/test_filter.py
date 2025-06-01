import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestFiltering(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://example.com")  # replace with your URL

    def test_filtering(self):
        # Navigate to a product category
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category']"))).click()

        # Wait for the filter sidebar to be present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@data-name='filter-sidebar']")))

        # Select a checkbox filter
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='size-xs']/input"))).click()

        # Wait for the page to update and verify that the number of visible product items is reduced
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-list']")))
        original_product_count = len(self.driver.find_elements(By.XPATH, "//div[@class='product-item']"))
        filtered_product_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-item']"))))
        self.assertLess(filtered_product_count, original_product_count)

        # Clear all filters
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-name='clear-all']"))).click()

        # Wait for the page to update and verify that the number of products returns to the original count
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-list']")))
        final_product_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-item']"))))
        self.assertEqual(final_product_count, original_product_count)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()