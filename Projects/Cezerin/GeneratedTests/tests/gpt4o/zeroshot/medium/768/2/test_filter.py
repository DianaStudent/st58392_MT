import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_apply_filters(self):
        driver = self.driver
        wait = self.wait

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = wait.until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Brand A']/preceding-sibling::input"))
        )
        self.assertIsNotNone(brand_a_checkbox, "Brand A checkbox not found or empty")
        brand_a_checkbox.click()
        time.sleep(2)  # Wait for UI to update

        # Verify the number of product cards changes
        products = driver.find_elements_by_css_selector('div.products > .available')
        self.assertEqual(len(products), 1, "Product count after applying 'Brand A' filter should be 1")

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)  # Wait for UI to update

        # Verify the original number of product cards is restored
        products = driver.find_elements_by_css_selector('div.products > .available')
        self.assertEqual(len(products), 2, "Product count after removing 'Brand A' filter should be 2")

        # Locate the price slider component and move it
        price_slider = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter .column"))
        )
        self.assertIsNotNone(price_slider, "Price slider not found or empty")

        slider_handle = driver.find_element_by_css_selector('.price-filter .noUi-handle')
        action = ActionChains(driver)
        action.click_and_hold(slider_handle).move_by_offset(-30, 0).release().perform()
        time.sleep(2)  # Wait for UI to update

        # Verify the product count changes again
        products = driver.find_elements_by_css_selector('div.products > .available')
        self.assertEqual(len(products), 1, "Product count after applying price filter should be 1")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()