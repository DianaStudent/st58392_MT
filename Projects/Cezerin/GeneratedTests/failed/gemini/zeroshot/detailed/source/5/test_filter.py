import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.url = "http://localhost:3000/category-a"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the category page (done in setUp)

        # 2. Wait until products and filters are fully loaded.
        product_locator = (By.CSS_SELECTOR, ".products .column a")
        self.wait.until(EC.presence_of_element_located(product_locator))

        # 3. Locate and apply the "Brand A" checkbox filter using its associated input.
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label/input[@type='checkbox']")
        brand_a_checkbox = self.wait.until(EC.presence_of_element_located(brand_a_checkbox_locator))

        # 4. Confirm it is checked.
        brand_a_checkbox.click()
        time.sleep(2)
        brand_a_checkbox_checked_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label[@class='attribute-checked']/input[@type='checkbox']")
        self.wait.until(EC.presence_of_element_located(brand_a_checkbox_checked_locator))

        # 5. Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 -> 1).
        product_cards_locator = (By.CSS_SELECTOR, ".products .column a")
        product_cards_after_filter = self.wait.until(EC.presence_of_all_elements_located(product_cards_locator))
        product_count_after_filter = len(product_cards_after_filter)
        self.assertEqual(product_count_after_filter, 1, "Product count should be 1 after applying 'Brand A' filter.")

        # 6. Uncheck the filter and confirm product count is restored (e.g., 1 -> 2).
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label[@class='attribute-checked']/input[@type='checkbox']")
        brand_a_checkbox = self.wait.until(EC.presence_of_element_located(brand_a_checkbox_locator))
        brand_a_checkbox.click()
        time.sleep(2)
        product_cards_locator = (By.CSS_SELECTOR, ".products .column a")
        product_cards_after_uncheck = self.wait.until(EC.presence_of_all_elements_located(product_cards_locator))
        product_count_after_uncheck = len(product_cards_after_uncheck)
        self.assertEqual(product_count_after_uncheck, 2, "Product count should be 2 after unchecking 'Brand A' filter.")

        # 7. Locate the price slider component and move the right slider handle to reduce the maximum price to 1159.
        price_filter_locator = (By.CLASS_NAME, "price-filter")
        price_filter = self.wait.until(EC.presence_of_element_located(price_filter_locator))

        right_slider_locator = (By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-right']")
        right_slider = self.wait.until(EC.presence_of_element_located(right_slider_locator))
        
        # Move the right slider
        actions = ActionChains(self.driver)
        actions.move_to_element(price_filter)
        actions.click_and_hold(right_slider)
        actions.move_by_offset(-30, 0)  # Adjust offset as needed
        actions.release().perform()

        # 8. Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 -> 1).
        time.sleep(2)
        product_cards_locator = (By.CSS_SELECTOR, ".products .column a")
        product_cards_after_price_filter = self.wait.until(EC.presence_of_all_elements_located(product_cards_locator))
        product_count_after_price_filter = len(product_cards_after_price_filter)
        self.assertEqual(product_count_after_price_filter, 1, "Product count should be 1 after applying price filter.")

if __name__ == "__main__":
    unittest.main()