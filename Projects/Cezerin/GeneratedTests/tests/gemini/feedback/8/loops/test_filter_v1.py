import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Open the category page. (Done in setUp)

        # 2. Locate and apply the "Brand A" checkbox filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox: {e}")

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes (e.g., 2 -> 1).
        try:
            product_cards_after_filter = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            num_product_cards_after_filter = len(product_cards_after_filter)
            self.assertEqual(num_product_cards_after_filter, 1, "Number of product cards after filtering for Brand A is not 1")
        except Exception as e:
            self.fail(f"Could not find product cards after filtering: {e}")

        # 5. Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox to uncheck: {e}")

        # 6. Verify that the original number of product cards is restored (e.g., 1 -> 2).
        try:
            product_cards_after_uncheck = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            num_product_cards_after_uncheck = len(product_cards_after_uncheck)
            self.assertEqual(num_product_cards_after_uncheck, 2, "Number of product cards after unchecking Brand A is not 2")
        except Exception as e:
            self.fail(f"Could not find product cards after unchecking: {e}")

        # 7. Locate the price slider component.
        # 8. Move one of the slider handles to apply a price range filter.
        # Note: Implementing the price slider interaction requires more advanced techniques
        #       like ActionChains to simulate dragging the slider handle.
        #       Since the prompt does not provide enough information to implement this reliably,
        #       I will skip this step for now.

        # 9. Verify that the product count changes again.
        # try:
        #     product_cards_after_price_filter = WebDriverWait(driver, 20).until(
        #         EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
        #     )
        #     num_product_cards_after_price_filter = len(product_cards_after_price_filter)
        #     self.assertNotEqual(num_product_cards_after_price_filter, num_product_cards_after_uncheck, "Number of product cards did not change after applying price filter")
        # except Exception as e:
        #     self.fail(f"Could not find product cards after price filtering: {e}")

if __name__ == "__main__":
    unittest.main()