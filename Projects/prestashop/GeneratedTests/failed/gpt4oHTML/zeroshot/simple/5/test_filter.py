from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestFilterFunctionality(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")  # Starting URL

    def test_filter_by_composition_matt_paper(self):
        driver = self.driver

        # Wait for the filter sidebar
        try:
            filter_sidebar = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'search_filters_wrapper'))
            )
        except Exception as e:
            self.fail("Filter sidebar not found: {}".format(e))
        
        # Get the initial number of products
        initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, '#js-product-list .product'))

        # Select the checkbox filter by label text "Composition" -> "Matt paper"
        try:
            composition_section = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//section[p[contains(text(), 'Composition')]]"))
            )
            matt_paper_checkbox = composition_section.find_element(By.XPATH, ".//span[label[contains(text(), 'Matt paper')]]/span/input")
            
            # Click on the checkbox to apply the filter
            matt_paper_checkbox.click()
        except Exception as e:
            self.fail("Unable to find and click on the 'Matt paper' filter: {}".format(e))

        # Wait until the product list is updated and confirm it by checking if the count changes
        WebDriverWait(driver, 20).until(
            EC.staleness_of(driver.find_elements(By.CSS_SELECTOR, '#js-product-list .product')[0])
        )
        
        try:
            filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, '#js-product-list .product'))
            self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying filter")
        except Exception as e:
            self.fail("Failed to verify product count after filter: {}".format(e))
        
        # Clear the filter by clicking the checkbox again
        try:
            matt_paper_checkbox.click()
            WebDriverWait(driver, 20).until(
                EC.staleness_of(driver.find_elements(By.CSS_SELECTOR, '#js-product-list .product')[0])
            )
            final_product_count = len(driver.find_elements(By.CSS_SELECTOR, '#js-product-list .product'))
            self.assertEqual(initial_product_count, final_product_count, "Product count did not revert after removing filter")
        except Exception as e:
            self.fail("Failed to clear filter and verify product count: {}".format(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()