from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def tearDown(self):
        self.driver.quit()

    def test_product_filters(self):
        # 1. Open the category page
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Category A")))
        self.driver.find_element(By.LINK_TEXT, "Category A").click()

        # Wait until products and filters are fully loaded.
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column")))

        # 3. Locate and apply the "Brand A" checkbox filter
        brand_filter = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[title='Brand A'] input")))
        brand_filter.click()

        # Confirm it is checked
        self.assertTrue(brand_filter.is_selected())

        # Wait 2 seconds and verify that the number of product cards is reduced.
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column")))
        original_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".available"))
        self.assertLess(original_product_count, 2)

        # Uncheck the filter and confirm product count is restored.
        brand_filter.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column")))
        new_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".available"))
        self.assertGreaterEqual(new_product_count, 2)

        # 7. Locate the price slider component and move the right slider handle
        price_slider = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-valuemin='0']")))
        ActionChains(self.driver).drag_and_drop_by_offset(price_slider, -30, 0).perform()

        # Wait 2 seconds and verify that the number of product cards is reduced.
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column")))
        new_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".available"))
        self.assertLess(new_product_count, original_product_count)

if __name__ == "__main__":
    unittest.main()