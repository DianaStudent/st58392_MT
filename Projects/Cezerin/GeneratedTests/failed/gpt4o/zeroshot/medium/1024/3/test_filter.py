from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Locate and apply the "Brand A" checkbox filter.
        brand_a_checkbox = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//label[.//input[@type='checkbox'] and contains(text(), 'Brand A')]"))
        )
        self.assertTrue(brand_a_checkbox, "Brand A checkbox is missing.")
        brand_a_checkbox.click()

        # Wait for UI update.
        driver.implicitly_wait(2)

        # Verify the number of displayed product cards decreases (2 -> 1).
        products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products), 1, "Product count should be 1 after Brand A filter applied.")

        # Uncheck the "Brand A" filter.
        brand_a_checkbox.click()

        # Verify the number of displayed product cards is restored (1 -> 2).
        products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products), 2, "Product count should be 2 after Brand A filter removed.")

        # Locate the price slider component.
        price_slider = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter-values"))
        )
        self.assertTrue(price_slider, "Price slider is missing.")
        
        # Use ActionChains to move the slider handle to apply a price range filter.
        slider_handle = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'price-filter-values')]/div[1]"))
        )
        action = ActionChains(driver)
        action.click_and_hold(slider_handle).move_by_offset(10, 0).release().perform()
        
        # Verify the product count changes after applying the price filter.
        products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products), 1, "Product count should change after price filter applied.")

if __name__ == "__main__":
    unittest.main()