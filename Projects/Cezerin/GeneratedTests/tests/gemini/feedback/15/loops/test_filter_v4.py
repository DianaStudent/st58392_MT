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
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filter_and_add_to_cart(self):
        driver = self.driver

        # 2. Locate and apply the "Brand A" checkbox filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            initial_product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column') and contains(@class, 'available')]"))
            )
            num_products_before_filter = len(initial_product_cards)
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox: {e}")

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes (e.g., 2 -> 1).
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column') and contains(@class, 'available')]"))
            )
            num_products_after_filter = len(product_cards)
            self.assertNotEqual(num_products_before_filter, num_products_after_filter, "Product count did not change after filtering.")
        except Exception as e:
            self.fail(f"Could not find product cards after filtering: {e}")

        # 5. Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or unclick 'Brand A' checkbox: {e}")

        # 6. Verify that the original number of product cards is restored (e.g., 1 -> 2).
        time.sleep(2)
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column') and contains(@class, 'available')]"))
            )
            num_products_after_unfilter = len(product_cards)
            self.assertEqual(num_products_before_filter, num_products_after_unfilter, "Product count did not restore after unfiltering.")
        except Exception as e:
            self.fail(f"Could not find product cards after unfiltering: {e}")

        # 7. Locate the price slider component.
        # 8. Move one of the slider handles to apply a price range filter.
        try:
            price_slider_handle = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']"))
            )
            actions = ActionChains(driver)
            actions.move_to_element(price_slider_handle).click_and_hold().move_by_offset(10, 0).release().perform()
        except Exception as e:
            self.fail(f"Could not find or move price slider handle: {e}")

        # 9. Verify that the product count changes again.
        time.sleep(2)
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column') and contains(@class, 'available')]"))
            )
            num_products_after_price_filter = len(product_cards)
            self.assertNotEqual(num_products_after_unfilter, num_products_after_price_filter, "Product count did not change after price filtering.")
        except Exception as e:
            self.fail(f"Could not find product cards after price filtering: {e}")

if __name__ == "__main__":
    unittest.main()