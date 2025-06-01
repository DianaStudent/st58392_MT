from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCartFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def tearDown(self):
        self.driver.quit()

    def test_product_filters(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Wait until products and filters are fully loaded
        filters_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".attribute-filter")))
        product_cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .available")))

        # Initial product count
        initial_product_count = len(product_cards)
        self.assertGreater(initial_product_count, 0, "Initial product count should be greater than 0")

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = filters_container.find_element(By.XPATH, ".//label[contains(text(), 'Brand A')]/input")
        brand_a_checkbox.click()
        time.sleep(2)

        # Confirm it is checked
        self.assertTrue(brand_a_checkbox.is_selected(), "Brand A checkbox should be selected")

        # Verify product count is reduced
        filtered_product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertLess(len(filtered_product_cards), initial_product_count, "Product count should be reduced after filter")

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Confirm product count is restored
        restored_product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(restored_product_cards), initial_product_count, "Product count should be restored after unchecking filter")

        # Locate the price slider component and move the right slider handle
        price_slider = driver.find_element(By.XPATH, "//div[@class='price-filter']//span[@aria-valuemax='1250.00']")
        driver.execute_script("arguments[0].setAttribute('aria-valuenow', '1159')", price_slider)
        driver.execute_script("arguments[0].style.left = '80%'", price_slider)
        time.sleep(2)

        # Verify the product count is reduced
        price_filtered_product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertLess(len(price_filtered_product_cards), initial_product_count, "Product count should be reduced after price filter")

if __name__ == "__main__":
    unittest.main()