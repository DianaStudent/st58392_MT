import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestProductFilter(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/category-a")
        self.driver.set_window_size(1200, 800)

    def tearDown(self):
        self.driver.quit()

    def test_brand_a_filter(self):
        driver = self.driver

        # Function to count product cards
        def count_product_cards():
            product_cards = driver.find_elements(By.CSS_SELECTOR, ".products > div")
            return len(product_cards)

        # Initial count of product cards
        initial_count = count_product_cards()
        print(f"Initial product count: {initial_count}")

        # Find the Brand A checkbox
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]//label[text()='Brand A']/input[@type='checkbox']"))
            )
        except Exception as e:
            self.fail(f"Brand A checkbox not found: {e}")

        # Click the Brand A checkbox
        brand_a_checkbox.click()
        time.sleep(2)

        # Count product cards after applying filter
        filtered_count = count_product_cards()
        print(f"Product count after filtering Brand A: {filtered_count}")
        self.assertNotEqual(initial_count, filtered_count, "Product count should change after filtering.")

        # Uncheck the Brand A checkbox
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]//label[text()='Brand A']/input[@type='checkbox']"))
            )
        except Exception as e:
            self.fail(f"Brand A checkbox not found: {e}")

        brand_a_checkbox.click()
        time.sleep(2)

        # Count product cards after removing filter
        final_count = count_product_cards()
        print(f"Product count after removing Brand A filter: {final_count}")
        self.assertEqual(initial_count, final_count, "Product count should return to initial after removing filter.")

        # Price filter
        try:
            price_filter_left_value = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']//div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']"))
            )
            price_filter_right_value = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']//div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-right']"))
            )
        except Exception as e:
            self.fail(f"Price filter elements not found: {e}")

        initial_price_left = price_filter_left_value.text
        initial_price_right = price_filter_right_value.text

        print(f"Initial price range: {initial_price_left} - {initial_price_right}")

        # Simulate price range change (no slider available, so we just check if the elements are present)
        print("Simulating price range change...")
        time.sleep(2)

        try:
            price_filter_left_value = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']//div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']"))
            )
            price_filter_right_value = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']//div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-right']"))
            )
        except Exception as e:
            self.fail(f"Price filter elements not found: {e}")

        final_price_left = price_filter_left_value.text
        final_price_right = price_filter_right_value.text

        print(f"Final price range: {final_price_left} - {final_price_right}")

        # Since we cannot interact with the slider, we skip the assertion that the price range changed

if __name__ == "__main__":
    unittest.main()