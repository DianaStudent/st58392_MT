import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on the "Art" category in the top menu
        art_category = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
        )
        art_category.click()

        # Step 3: Wait for the category page to load
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#js-product-list"))
        )

        # Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        composition_filter = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Matt paper']/preceding-sibling::span/input[@type='checkbox']"))
        )
        composition_filter.click()

        # Step 6: Wait for the filter to apply
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".products .js-product"))
        )

        # Step 7: Assert that the number of product tiles is reduced from 7 to 3
        products = driver.find_elements(By.CSS_SELECTOR, ".products .js-product")
        self.assertEqual(len(products), 3, "The number of product tiles after applying the filter is not 3")

        # Step 8: Locate and click the "Clear all" button to remove filters
        clear_filter = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'ok')]"))
        )
        clear_filter.click()

        # Step 9: Wait and assert that the number of products returns to the original count - 7
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".products .js-product"))
        )
        products = driver.find_elements(By.CSS_SELECTOR, ".products .js-product")
        self.assertEqual(len(products), 7, "The number of product tiles after clearing the filter is not 7")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()