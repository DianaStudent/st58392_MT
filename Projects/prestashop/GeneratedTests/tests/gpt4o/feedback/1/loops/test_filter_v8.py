import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filter_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on the "Art" category in the top menu
        art_category_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/en/9-art')]"))
        )
        art_category_link.click()

        # Step 3: Wait for the category page to load
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Art')]")))

        # Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        filter_sidebar = wait.until(EC.presence_of_element_located((By.ID, "search_filters")))

        # Locate "Matt paper" checkbox using label text
        composition_filter = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Matt paper')]/preceding-sibling::input"))
        )
        composition_filter.click()

        # Step 5: Wait for the filter to apply by ensuring the product list updates
        wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".products .js-product")) == 3)

        # Step 6: Assert the number of product tiles is reduced to 3
        products = driver.find_elements(By.CSS_SELECTOR, ".products .js-product")
        self.assertEqual(len(products), 3, "Product count after filtering should be 3.")

        # Step 7: Clear the filter
        # Since no “Clear all” button is provided, re-accessing the category page can reset filters
        driver.get("http://localhost:8080/en/9-art")

        # Step 8: Verify that the original product count returns
        wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".products .js-product")) == 7)
        products_after_clearing = driver.find_elements(By.CSS_SELECTOR, ".products .js-product")
        self.assertEqual(len(products_after_clearing), 7, "Product count after clearing filters should be 7.")

if __name__ == "__main__":
    unittest.main()