import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the category page. (Done in setUp)

        # 2. Wait until products and filters are fully loaded.
        product_locator = (By.CSS_SELECTOR, ".products .column a")
        wait.until(EC.presence_of_element_located(product_locator))

        # Get initial product count
        products = driver.find_elements(*product_locator)
        initial_product_count = len(products)
        if initial_product_count == 0:
            self.fail("Initial product count is zero.")

        # 3. Locate and apply the "Brand A" checkbox filter using its associated input.
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']")
        brand_a_checkbox = wait.until(EC.presence_of_element_located(brand_a_checkbox_locator))
        brand_a_checkbox.click()

        # 4. Confirm it is checked.
        brand_a_label_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]")
        brand_a_label = wait.until(EC.presence_of_element_located(brand_a_label_locator))
        self.assertIn("attribute-checked", brand_a_label.get_attribute("class"), "Brand A checkbox is not checked.")

        # 5. Wait 2 seconds and verify that the number of product cards is reduced.
        time.sleep(2)
        products = driver.find_elements(*product_locator)
        filtered_product_count = len(products)
        self.assertLess(filtered_product_count, initial_product_count, "Product count was not reduced after filtering.")

        # 6. Uncheck the filter and confirm product count is restored.
        brand_a_checkbox = wait.until(EC.presence_of_element_located(brand_a_checkbox_locator))
        brand_a_checkbox.click()
        time.sleep(2)
        products = driver.find_elements(*product_locator)
        restored_product_count = len(products)
        self.assertEqual(restored_product_count, initial_product_count, "Product count was not restored after unchecking the filter.")

        # 7. Locate the price slider component and move the right slider handle to reduce the maximum price to 1159.
        price_filter_values_locator = (By.CLASS_NAME, "price-filter-values")
        price_filter_values = wait.until(EC.presence_of_element_located(price_filter_values_locator))

        right_slider_locator = (By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[2]")
        right_slider = wait.until(EC.presence_of_element_located(right_slider_locator))

        actions = ActionChains(driver)
        actions.click_and_hold(right_slider).move_by_offset(-10, 0).release().perform()
        time.sleep(1)

        # 8. Wait 2 seconds and verify that the number of product cards is reduced.
        time.sleep(2)
        products = driver.find_elements(*product_locator)
        final_product_count = len(products)
        self.assertLess(final_product_count, restored_product_count, "Product count was not reduced after price filtering.")

if __name__ == "__main__":
    unittest.main()