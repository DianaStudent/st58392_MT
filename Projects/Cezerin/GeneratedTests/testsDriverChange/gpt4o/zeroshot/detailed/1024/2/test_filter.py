from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/category-a')

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Wait for products and filters to load
        product_selector = (By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products")
        filter_selector = (By.CLASS_NAME, "attribute-filter")
        
        wait.until(EC.presence_of_element_located(product_selector))
        wait.until(EC.presence_of_element_located(filter_selector))

        # Locate and apply "Brand A" checkbox filter
        brand_a_checkbox = driver.find_element(By.XPATH, "//label[input[@type='checkbox' and following-sibling::text()[contains(., 'Brand A')]]]/input")
        brand_a_checkbox.click()

        # Confirm it is checked
        self.assertTrue(brand_a_checkbox.is_selected())

        # Wait 2 seconds to verify product count reduction
        time.sleep(2)
        products = driver.find_elements(By.CSS_SELECTOR, ".product-name")
        self.assertEqual(len(products), 1, "Product count should be reduced to 1 with Brand A filter applied")

        # Uncheck the filter
        brand_a_checkbox.click()
        self.assertFalse(brand_a_checkbox.is_selected())

        # Wait 2 seconds to verify product count restoration
        time.sleep(2)
        products = driver.find_elements(By.CSS_SELECTOR, ".product-name")
        self.assertEqual(len(products), 2, "Product count should be restored to 2 after removing the Brand A filter")

        # Locate the price slider and adjust it
        max_slider = driver.find_element(By.XPATH, "//div[@class='price-filter']//input[@type='range' and @aria-valuemax]")
        actions = ActionChains(driver)

        # Adjust the slider to set maximum price to 1159
        actions.click_and_hold(max_slider).move_by_offset(-50, 0).release().perform()

        # Confirm slider was adjusted
        max_value = int(max_slider.get_attribute('aria-valuenow'))
        self.assertLessEqual(max_value, 1159, "Maximum price should be adjusted to 1159 or less")

        # Wait 2 seconds to verify product count reduction
        time.sleep(2)
        products = driver.find_elements(By.CSS_SELECTOR, ".product-name")
        self.assertEqual(len(products), 1, "Product count should be reduced to 1 with the price filter applied")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()