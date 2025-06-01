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
        self.url = "http://localhost:3000/category-a"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_filter_and_add_to_cart(self):
        # 1. Open the category page (done in setUp)
        # 2. Wait until products and filters are fully loaded.
        product_locator = (By.CSS_SELECTOR, ".products .column a")
        self.wait.until(EC.presence_of_all_elements_located(product_locator))

        # Initial product count
        initial_products = self.driver.find_elements(*product_locator)
        initial_product_count = len(initial_products)

        # 3. Locate and apply the "Brand A" checkbox filter using its associated input.
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label/input[@type='checkbox']")
        try:
            brand_a_checkbox = self.wait.until(EC.presence_of_element_located(brand_a_checkbox_locator))
        except:
            self.fail("Brand A checkbox not found")

        # 4. Confirm it is checked.
        brand_a_checkbox.click()
        time.sleep(2)

        brand_a_checked_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label[@class='attribute-checked']/input[@type='checkbox']")
        try:
            self.wait.until(EC.presence_of_element_located(brand_a_checked_locator))
        except:
            self.fail("Brand A checkbox not checked")

        # 5. Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 -> 1).
        time.sleep(2)
        filtered_products = self.driver.find_elements(*product_locator)
        filtered_product_count = len(filtered_products)
        self.assertLess(filtered_product_count, initial_product_count, "Product count was not reduced after filtering by Brand A")

        # 6. Uncheck the filter and confirm product count is restored (e.g., 1 -> 2).
        try:
            brand_a_checkbox = self.wait.until(EC.presence_of_element_located(brand_a_checked_locator))
        except:
            self.fail("Brand A checkbox not found")
        brand_a_checkbox.click()
        time.sleep(2)

        unfiltered_products = self.driver.find_elements(*product_locator)
        unfiltered_product_count = len(unfiltered_products)
        self.assertEqual(unfiltered_product_count, initial_product_count, "Product count was not restored after unchecking Brand A")

        # 7. Locate the price slider component and move the right slider handle to reduce the maximum price to 1159.
        price_filter_locator = (By.CLASS_NAME, "price-filter")
        try:
            price_filter = self.wait.until(EC.presence_of_element_located(price_filter_locator))
        except:
            self.fail("Price filter not found")

        right_slider_locator = (By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-right']")
        try:
            right_slider = self.wait.until(EC.presence_of_element_located(right_slider_locator))
        except:
            self.fail("Right slider handle not found")

        # Get the current maximum price
        current_max_price_text = right_slider.text
        current_max_price = float(current_max_price_text.replace('$', '').replace(',', ''))

        # Calculate the offset to move the slider to the desired price
        desired_max_price = 1159.00
        offset = int((desired_max_price - current_max_price) / (1250.00 - 967.00) * right_slider.size['width'])

        actions = ActionChains(self.driver)
        actions.click_and_hold(right_slider).move_by_offset(offset, 0).release().perform()

        # 8. Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 -> 1).
        time.sleep(2)
        price_filtered_products = self.driver.find_elements(*product_locator)
        price_filtered_product_count = len(price_filtered_products)
        self.assertLess(price_filtered_product_count, unfiltered_product_count, "Product count was not reduced after price filtering")

if __name__ == "__main__":
    unittest.main()