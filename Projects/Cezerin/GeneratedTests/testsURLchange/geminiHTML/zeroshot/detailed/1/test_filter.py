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

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Wait until products are loaded
        products_locator = (By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products")
        wait.until(EC.presence_of_element_located(products_locator))

        # Get initial product count
        product_cards_locator = (By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div")
        initial_product_cards = driver.find_elements(*product_cards_locator)
        initial_product_count = len(initial_product_cards)

        # Locate "Brand A" checkbox
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute']//div[contains(text(),'Brand')]/following-sibling::label[contains(.,'Brand A')]/input[@type='checkbox']")
        brand_a_checkbox = wait.until(EC.presence_of_element_located(brand_a_checkbox_locator))

        # Apply "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify "Brand A" is checked
        brand_a_checked_locator = (By.XPATH, "//div[@class='attribute']//div[contains(text(),'Brand')]/following-sibling::label[contains(@class,'attribute-checked') and contains(.,'Brand A')]/input[@type='checkbox']")
        wait.until(EC.presence_of_element_located(brand_a_checked_locator))

        # Get product count after filtering
        product_cards_after_filter = driver.find_elements(*product_cards_locator)
        product_count_after_filter = len(product_cards_after_filter)

        self.assertNotEqual(initial_product_count, product_count_after_filter, "Product count should change after applying the filter.")

        # Uncheck the filter
        brand_a_checkbox = wait.until(EC.presence_of_element_located(brand_a_checkbox_locator))
        brand_a_checkbox.click()
        time.sleep(2)

        # Get product count after removing filter
        product_cards_after_uncheck = driver.find_elements(*product_cards_locator)
        product_count_after_uncheck = len(product_cards_after_uncheck)

        self.assertEqual(initial_product_count, product_count_after_uncheck, "Product count should return to initial count after removing the filter.")

        # Locate price slider handle
        price_slider_handle_locator = (By.XPATH, "//div[@class='price-filter']//div[@class='columns is-mobile is-gapless price-filter-values']/following-sibling::div//span[2]")
        price_slider_handle = wait.until(EC.presence_of_element_located(price_slider_handle_locator))

        # Move the slider
        actions = ActionChains(driver)
        actions.click_and_hold(price_slider_handle).move_by_offset(-20, 0).release().perform()
        time.sleep(2)

        # Get product count after price filtering
        product_cards_after_price_filter = driver.find_elements(*product_cards_locator)
        product_count_after_price_filter = len(product_cards_after_price_filter)

        self.assertNotEqual(initial_product_count, product_count_after_price_filter, "Product count should change after price filtering.")

if __name__ == "__main__":
    unittest.main()