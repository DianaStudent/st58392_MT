from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_apply_filters(self):
        driver = self.driver
        wait = self.wait

        # Wait until products and filters are fully loaded
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".section-category")))

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[.//input[@type='checkbox' and preceding-sibling::text()='Brand A']]")))
        brand_a_checkbox.click()
        
        # Confirm the checkbox is checked
        checkbox_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[.//input[@type='checkbox' and preceding-sibling::text()='Brand A']]/input")))
        self.assertTrue(checkbox_input.is_selected())

        # Wait 2 seconds and verify the number of product cards is reduced
        driver.implicitly_wait(2)
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .product-caption")))
        self.assertEqual(len(products), 1)

        # Uncheck the filter
        brand_a_checkbox.click()
        driver.implicitly_wait(2)

        # Confirm the product count is restored
        products_restored = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .product-caption")))
        self.assertEqual(len(products_restored), 2)

        # Locate the price slider
        slider = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='price-filter']//input[@aria-valuemax='1250']")))

        # Move the right slider handle to reduce the maximum price
        action = ActionChains(driver)
        action.click_and_hold(slider).move_by_offset(-20, 0).release().perform()

        # Confirm slider value change
        self.assertEqual(slider.get_attribute("aria-valuemax"), '1159')

        # Wait 2 seconds and verify the number of product cards is reduced
        driver.implicitly_wait(2)
        products_after_price = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .product-caption")))
        self.assertEqual(len(products_after_price), 1)


if __name__ == "__main__":
    unittest.main()