import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a")

    def tearDown(self):
        self.driver.quit()

    def test_product_filter_by_brand_and_price(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Wait for product and filters to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.products .column.available')))

        # Locate the brand checkbox for Brand A
        brand_a_checkbox = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='attribute'][div/text()='Brand']/label[input and contains(text(), 'Brand A')]" +
                 "/input")
            )
        )

        # Get initial count of visible product cards
        initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, '.products .column.available'))

        # Click Brand A filter and wait
        brand_a_checkbox.click()
        time.sleep(2)

        # Ensure the filter checkbox is checked
        self.assertTrue(brand_a_checkbox.is_selected(), "Brand A checkbox is not selected.")

        # Verify the number of product cards is reduced (2 -> 1)
        reduced_product_count = len(driver.find_elements(By.CSS_SELECTOR, '.products .column.available'))
        self.assertLess(reduced_product_count, initial_product_count, "Product count did not reduce.")

        # Uncheck Brand A
        brand_a_checkbox.click()
        time.sleep(2)

        # Confirm product count is restored (1 -> 2)
        restored_product_count = len(driver.find_elements(By.CSS_SELECTOR, '.products .column.available'))
        self.assertEqual(restored_product_count, initial_product_count, "Product count did not restore.")

        # Locate the price slider
        price_slider = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='price-filter']//input[@type='range' and @aria-valuenow]"))
        )

        # Move the right slider handle
        slider_min = float(price_slider.get_attribute("aria-valuemin"))
        slider_max = float(price_slider.get_attribute("aria-valuemax"))
        
        # Calculate offset to move the slider
        offset = (1159 - slider_min) / (slider_max - slider_min) * 100

        actions = ActionChains(driver)
        actions.click_and_hold(price_slider).move_by_offset(offset, 0).release().perform()
        time.sleep(2)

        # Verify the number of product cards is reduced again (2 -> 1)
        final_product_count = len(driver.find_elements(By.CSS_SELECTOR, '.products .column.available'))
        self.assertLess(final_product_count, restored_product_count, "Product count did not reduce after price filter.")

if __name__ == "__main__":
    unittest.main()