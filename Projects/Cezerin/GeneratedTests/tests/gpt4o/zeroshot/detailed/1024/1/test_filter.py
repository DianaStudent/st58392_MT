from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class TestCategoryFilter(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.base_url = "http://localhost:3000/category-a"

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # Wait until products and filters are fully loaded
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'section.section-category .products'))
        )

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = driver.find_element(By.XPATH, "//div[@class='attribute-title' and contains(text(),'Brand')]/following-sibling::label[1]//input")
        self.assertTrue(brand_a_checkbox, "Brand A checkbox not found")
        brand_a_checkbox.click()
        time.sleep(2)

        # Confirm it is checked
        self.assertTrue(brand_a_checkbox.is_selected(), "Brand A checkbox is not checked after clicking")

        # Verify that the number of product cards is reduced (e.g., 2 → 1)
        products = driver.find_elements(By.CSS_SELECTOR, '.products .column.is-6-mobile')
        self.assertEqual(len(products), 1, "Product count did not reduce after applying Brand A filter")

        # Uncheck the filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Confirm product count is restored (e.g., 1 → 2)
        products = driver.find_elements(By.CSS_SELECTOR, '.products .column.is-6-mobile')
        self.assertEqual(len(products), 2, "Product count did not restore after removing Brand A filter")

        # Locate the price slider component and move the right slider handle
        slider_right_handle = driver.find_element(By.XPATH, "//div[@class='price-filter']/descendant::div[@aria-valuemax]")
        assert slider_right_handle, "Price slider max handle not found"

        # Adjust slider using JavaScript
        driver.execute_script("arguments[0].setAttribute('aria-valuenow', '1159')", slider_right_handle)
        time.sleep(2)

        # Verify that the number of product cards is reduced (e.g., 2 → 1)
        products = driver.find_elements(By.CSS_SELECTOR, '.products .column.is-6-mobile')
        self.assertEqual(len(products), 1, "Product count did not reduce after moving price slider")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()