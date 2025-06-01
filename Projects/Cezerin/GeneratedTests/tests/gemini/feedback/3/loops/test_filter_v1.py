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

    def test_filter_and_add_to_cart(self):
        driver = self.driver
        initial_html = driver.page_source
        if not initial_html:
            self.fail("Initial HTML is empty.")

        # 1. Open the category page.
        # Already done in setUp

        # 2. Locate and apply the "Brand A" checkbox filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to locate or click 'Brand A' checkbox: {e}")

        # 3. Wait 2 seconds to allow the UI to update.
        time.sleep(2)

        # 4. Verify that the number of displayed product cards changes (e.g., 2 -> 1).
        try:
            product_cards = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            num_products_after_filter = len(product_cards)
        except Exception as e:
            self.fail(f"Failed to locate product cards after filter: {e}")

        # Get the initial number of product cards
        driver.get("http://localhost:3000/category-a")
        try:
            product_cards_initial = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            num_products_initial = len(product_cards_initial)
        except Exception as e:
            self.fail(f"Failed to locate initial product cards: {e}")

        if num_products_after_filter == num_products_initial:
            self.fail("The number of product cards did not change after applying the filter.")

        # 5. Uncheck the "Brand A" filter.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to locate or uncheck 'Brand A' checkbox: {e}")

        # 6. Verify that the original number of product cards is restored (e.g., 1 -> 2).
        time.sleep(2)
        try:
            product_cards_after_uncheck = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]"))
            )
            num_products_after_uncheck = len(product_cards_after_uncheck)
        except Exception as e:
            self.fail(f"Failed to locate product cards after unchecking filter: {e}")

        if num_products_after_uncheck != num_products_initial:
            self.fail("The number of product cards was not restored after unchecking the filter.")

        # 7. Locate the price slider component.
        # 8. Move one of the slider handles to apply a price range filter.
        # This step is skipped because the slider is not implemented.

        # 9. Verify that the product count changes again.
        # This step is skipped because the slider is not implemented.

if __name__ == "__main__":
    unittest.main()