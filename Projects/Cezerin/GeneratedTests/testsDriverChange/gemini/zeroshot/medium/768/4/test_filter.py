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

    def test_filter_and_add_to_cart(self):
        driver = self.driver

        # 1. Open the category page - Done in setUp

        # 2. Locate and apply the "Brand A" checkbox filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
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
            initial_product_count = len(product_cards)
            self.assertTrue(initial_product_count > 0, "Initial product count should be greater than 0")

            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()

            time.sleep(2)

            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column') and contains(@class, 'available')]"))
            )
            final_product_count = len(product_cards)
            self.assertTrue(final_product_count > 0, "Final product count should be greater than 0")
            self.assertNotEqual(initial_product_count, final_product_count, "Product count should change after filtering")
        except Exception as e:
            self.fail(f"Failed to verify product count change: {e}")

        # 5. Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not uncheck 'Brand A' checkbox: {e}")

        # 6. Verify that the original number of product cards is restored (e.g., 1 -> 2).
        time.sleep(2)

        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column') and contains(@class, 'available')]"))
            )
            restored_product_count = len(product_cards)
            self.assertEqual(initial_product_count, restored_product_count, "Product count should be restored after unchecking filter")
        except Exception as e:
            self.fail(f"Failed to verify product count restoration: {e}")

        # 7. Locate the price slider component.
        # 8. Move one of the slider handles to apply a price range filter.
        try:
            # Locate the left price handle
            price_filter_values = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-filter-values"))
            )

            # Extract the current minimum price
            min_price_element = price_filter_values.find_element(By.CLASS_NAME, "has-text-left")
            min_price_text = min_price_element.text
            min_price = float(min_price_text.replace('$', '').replace(',', ''))

            # Increase the minimum price by 17
            new_min_price = min_price + 17

            # Locate the price filter values again to ensure it's up-to-date
            price_filter_values = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-filter-values"))
            )

            # Update the minimum price text
            new_min_price_text = "${:,.2f}".format(new_min_price)
            driver.execute_script(f"arguments[0].innerText = '{new_min_price_text}';", min_price_element)

        except Exception as e:
            self.fail(f"Failed to manipulate price slider: {e}")

        # 9. Verify that the product count changes again.
        time.sleep(2)

        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column') and contains(@class, 'available')]"))
            )
            filtered_product_count = len(product_cards)
            self.assertNotEqual(restored_product_count, filtered_product_count, "Product count should change after price filtering")
        except Exception as e:
            self.fail(f"Failed to verify product count change after price filtering: {e}")

if __name__ == "__main__":
    unittest.main()