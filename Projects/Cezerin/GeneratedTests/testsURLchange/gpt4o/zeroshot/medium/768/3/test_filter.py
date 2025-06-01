from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "app")))

    def tearDown(self):
        self.driver.quit()

    def test_apply_product_filter(self):
        driver = self.driver

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Brand A')]/input")))
        brand_a_checkbox.click()

        # Wait 2 seconds to allow the UI to update
        time.sleep(2)

        # Verify that number of displayed product cards changes
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(product_cards), 1, "Expected 1 product after filtering by Brand A.")

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()

        # Wait 2 seconds to allow the UI to update
        time.sleep(2)

        # Verify that the original number of product cards is restored
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(product_cards), 2, "Expected 2 products after removing Brand A filter.")

        # Locate the price slider component
        price_slider = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter .column.has-text-left")))

        # Move one of the slider handles to apply price range filter
        actions = ActionChains(driver)
        actions.click_and_hold(price_slider).move_by_offset(10, 0).release().perform()

        # Wait 2 seconds to allow the UI to update
        time.sleep(2)

        # Verify that the product count changes again
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(product_cards), 1, "Expected 1 product after applying price filter.")

if __name__ == "__main__":
    unittest.main()