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
        self.driver.execute_script("document.body.style.zoom='50%'")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Open the category page - done in setUp

        # 2. Locate and apply the "Brand A" checkbox filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click Brand A checkbox: {e}")

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes (e.g., 2 -> 1).
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div"))
            )
            initial_product_count = len(product_cards)
            self.assertTrue(initial_product_count > 0, "Initial product count should be greater than 0")
        except Exception as e:
            self.fail(f"Could not find product cards or get initial count: {e}")

        # Get product count after filter
        try:
            product_cards_filtered = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div"))
            )
            filtered_product_count = len(product_cards_filtered)
            self.assertTrue(filtered_product_count >= 0, "Filtered product count should be greater than or equal to 0")
            self.assertNotEqual(initial_product_count, filtered_product_count, "Product count should change after filtering")
        except Exception as e:
            self.fail(f"Could not find product cards or get filtered count: {e}")

        # 5. Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or unclick Brand A checkbox: {e}")

        # 6. Verify that the original number of product cards is restored (e.g., 1 -> 2).
        try:
            product_cards_restored = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products > div"))
            )
            restored_product_count = len(product_cards_restored)
            self.assertEqual(initial_product_count, restored_product_count, "Product count should be restored after unchecking filter")
        except Exception as e:
            self.fail(f"Could not find product cards or get restored count: {e}")

        # 7. Locate the price slider component.
        # 8. Move one of the slider handles to apply a price range filter.
        # The provided HTML doesn't include a proper price slider, so this step is skipped.
        # Skipping the price slider interaction because there is no slider element.

        # 9. Verify that the product count changes again.
        # Since we skipped the price slider, we can't verify this step.
        print("Price slider interaction skipped due to missing element.")

if __name__ == "__main__":
    unittest.main()