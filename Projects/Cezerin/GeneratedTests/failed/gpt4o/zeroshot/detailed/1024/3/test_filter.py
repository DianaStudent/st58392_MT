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

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_apply_product_filter(self):
        driver = self.driver

        # Wait until products and filters are fully loaded
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".section-category")))

        # Locate and apply the "Brand A" checkbox filter using its associated input
        brand_a_checkbox = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//label[input[@type='checkbox'] and contains(., 'Brand A')]"))
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Confirm it is checked
        self.assertTrue(brand_a_checkbox.find_element_by_tag_name("input").is_selected(), "Brand A checkbox is not checked.")

        # Verify that the number of product cards is reduced
        products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products), 1, "Product count should be reduced to 1 after filtering by Brand A.")

        # Uncheck the filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Confirm product count is restored
        products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products), 2, "Product count should be restored to 2 after removing Brand A filter.")

        # Locate the price slider component
        price_slider = driver.find_element(By.CSS_SELECTOR, ".price-filter .attribute-title + div")
        actions = ActionChains(driver)

        # Move the right slider handle to reduce the maximum price to 1159
        right_handle = price_slider.find_elements_by_tag_name("span")[2]
        actions.click_and_hold(right_handle).move_by_offset(-50, 0).release().perform()
        time.sleep(2)

        # Verify that the number of product cards is reduced
        products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products), 1, "Product count should be reduced to 1 after adjusting price slider.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()