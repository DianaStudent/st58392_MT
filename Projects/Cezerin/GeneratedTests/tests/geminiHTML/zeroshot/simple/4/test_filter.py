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
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_brand_a_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Function to count product cards
        def count_product_cards():
            product_elements = driver.find_elements(By.CSS_SELECTOR, ".products > div")
            return len(product_elements)

        # Initial product count
        initial_product_count = count_product_cards()
        print(f"Initial product count: {initial_product_count}")

        # Find the Brand A checkbox and click it
        try:
            brand_a_checkbox = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click Brand A checkbox: {e}")

        time.sleep(2)

        # Get product count after applying filter
        filtered_product_count = count_product_cards()
        print(f"Product count after applying Brand A filter: {filtered_product_count}")
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count should change after applying the filter")

        # Uncheck the Brand A checkbox
        try:
            brand_a_checkbox = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or unclick Brand A checkbox: {e}")

        time.sleep(2)

        # Get product count after removing filter
        unfiltered_product_count = count_product_cards()
        print(f"Product count after removing Brand A filter: {unfiltered_product_count}")
        self.assertEqual(initial_product_count, unfiltered_product_count, "Product count should return to initial value after removing the filter")

        # Price Filter
        try:
            price_filter_left_handle = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter-values > div:first-child"))
            )
            price_filter_right_handle = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter-values > div:last-child"))
            )
        except Exception as e:
            self.fail(f"Could not find price filter handles: {e}")

        initial_product_count_price_filter = count_product_cards()

        # Move the left handle of the price filter
        try:
            actions = ActionChains(driver)
            actions.move_to_element(price_filter_left_handle).click_and_hold(price_filter_left_handle).move_by_offset(10, 0).release().perform()
        except Exception as e:
            self.fail(f"Could not move left handle of price filter: {e}")

        time.sleep(2)

        filtered_product_count_price_filter = count_product_cards()
        print(f"Product count after price filter: {filtered_product_count_price_filter}")
        self.assertNotEqual(initial_product_count_price_filter, filtered_product_count_price_filter, "Product count should change after applying the price filter")


if __name__ == "__main__":
    unittest.main()