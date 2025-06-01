from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://your-shop-url.com')

    def test_filters(self):
        # 1. Open the category page.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        self.driver.find_element(By.XPATH, "//a[@href='/category-a']").click()

        # 2. Wait until products and filters are fully loaded.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products")))

        # 3. Locate and apply the "Brand A" checkbox filter using its associated input.
        brand_a_checkbox = self.driver.find_element(By.XPATH, "//input[@value='Brand A']")
        brand_a_checkbox.click()

        # 4. Confirm it is checked.
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//label[@for='Brand-A']")))
        self.assertTrue(brand_a_checkbox.is_selected())

        # 5. Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 → 1).
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-caption")))
        self.assertLess(len(self.driver.find_elements(By.CSS_SELECTOR, ".product-caption")), len(self.driver.find_elements(By.XPATH, "//a[@href='/category-a/product-b']")))

        # 6. Uncheck the filter and confirm product count is restored (e.g., 1 → 2).
        brand_a_checkbox.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-caption")))
        self.assertGreaterEqual(len(self.driver.find_elements(By.CSS_SELECTOR, ".product-caption")), len(self.driver.find_elements(By.XPATH, "//a[@href='/category-a/product-b']")))

        # 7. Locate the price slider component and move the right slider handle to reduce the maximum price to 1159.
        price_slider = self.driver.find_element(By.XPATH, "//input[@aria-valuemin='0']")
        aria_valuenow = int(self.driver.execute_script("return arguments[0].getAttribute('aria-valuenow');", price_slider))
        aria_max = int(self.driver.execute_script("return arguments[0].getAttribute('aria-valuemax');", price_slider))

        while aria_valuenow < 1159:
            aria_valuenow += 1
            self.driver.execute_script("arguments[0].setAttribute('aria-valuenow', '" + str(aria_valuenow) + "');", price_slider)
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-valuemin='0']")))
        else:
            self.fail("Failed to move slider handle")

        # 9. Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 → 1).
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-caption")))
        self.assertLess(len(self.driver.find_elements(By.CSS_SELECTOR, ".product-caption")), len(self.driver.find_elements(By.XPATH, "//a[@href='/category-a/product-b']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()