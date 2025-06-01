from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductFilters(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filters(self):
        driver = self.driver

        # Step 2: Wait until products and filters are fully loaded
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.columns.is-multiline.is-mobile.products"))
        )

        # Step 3: Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[contains(text(),'Brand A')]/input"))
        )
        brand_a_checkbox.click()
        time.sleep(2)  # Wait for the filter to be applied

        # Step 4: Confirm Brand A filter is checked
        self.assertTrue(brand_a_checkbox.is_selected(), "Brand A checkbox is not selected!")

        # Step 5: Verify that number of product cards is reduced
        filtered_products = driver.find_elements(By.CSS_SELECTOR, "div.column.is-6-mobile.is-4-tablet")
        self.assertEqual(len(filtered_products), 1, "Product count did not reduce after applying filter!")

        # Step 6: Uncheck the filter
        brand_a_checkbox.click()
        time.sleep(2)  # Wait for the filter to be removed

        # Verify product count is restored
        unfiltered_products = driver.find_elements(By.CSS_SELECTOR, "div.column.is-6-mobile.is-4-tablet")
        self.assertEqual(len(unfiltered_products), 2, "Product count did not restore after removing filter!")

        # Step 7: Locate the price slider component and move right handle
        price_slider = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".price-filter-values .column.has-text-right"))
        )
        slider_handle = driver.find_element(
            By.XPATH, "//div[@class='price-filter']//input[@type='range' and @aria-valuemax='1250']")
        
        # Move the slider handle
        ActionChains(driver).click_and_hold(slider_handle).move_by_offset(-20, 0).release().perform()
        time.sleep(2)  # Wait for the filter to be applied

        # Step 9: Verify product count is reduced
        reduced_products = driver.find_elements(By.CSS_SELECTOR, "div.column.is-6-mobile.is-4-tablet")
        self.assertEqual(len(reduced_products), 1, "Product count did not reduce after applying price filter!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()