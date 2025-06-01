from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
    
    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Click on "Art" category
        art_category = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.dropdown-item[href*="/9-art"]'))
        )
        art_category.click()

        # Wait for the Art category page to load
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div#js-product-list'))
        )
        
        # Locate and apply "Matt paper" filter under "Composition"
        composition_filter = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "Composition-Matt+paper")]'))
        )
        composition_filter.click()
        
        # Wait for the filter to apply and assert the product count is reduced to 3
        wait.until(
            lambda driver: len(driver.find_elements(By.CSS_SELECTOR, 'div.js-product')) == 3,
            message='Product count did not reduce to 3 after filter applied'
        )

        # Locate and click "Clear all" filters button
        clear_filters_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#js-active-search-filters'))
        )
        if clear_filters_button.is_displayed():
            clear_filters_button.click()
        else:
            self.fail('Clear all filters button not found')
        
        # Assert the product count returns to 7
        wait.until(
            lambda driver: len(driver.find_elements(By.CSS_SELECTOR, 'div.js-product')) == 7,
            message='Product count did not return to 7 after clearing filters'
        )
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()