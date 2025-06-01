import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_brand_a_filter(self):
        # Initial number of products
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        initial_product_count = len(products)

        # Apply Brand A filter
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']")
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Number of products after applying filter
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        filtered_product_count = len(products)

        # Uncheck Brand A filter
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Number of products after removing filter
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        final_product_count = len(products)

        # Assert that the product count changed after applying and removing the filter
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count should change after applying filter")
        self.assertEqual(initial_product_count, final_product_count, "Product count should return to initial after removing filter")

    def test_price_filter(self):
        # Initial number of products
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        initial_product_count = len(products)

        # Price filter slider
        price_filter_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Price']/following-sibling::div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']")
        price_filter = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(price_filter_locator)
        )

        # Move the slider
        actions = ActionChains(self.driver)
        actions.move_to_element(price_filter).move_by_offset(10, 0).click().perform()
        time.sleep(2)

        # Number of products after applying filter
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        filtered_product_count = len(products)

        # Assert that the product count changed after applying the filter
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count should change after applying filter")

if __name__ == "__main__":
    unittest.main()