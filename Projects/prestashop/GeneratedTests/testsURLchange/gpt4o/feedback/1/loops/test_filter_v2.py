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
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Art')]"))
        )
        art_category_link.click()

        # Step 3: Wait for the category page to load
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Art')]")))

        # Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        composition_filter = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[contains(., 'Matt paper')]//input[@type='checkbox']")
            )
        )
        composition_filter.click()

        # Step 5: Wait for the filter to apply
        wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .js-product"))
        )

        # Step 6: Assert the number of product tiles is reduced to 3
        products = driver.find_elements(By.CSS_SELECTOR, ".products .js-product")
        self.assertEqual(len(products), 3, "Product count after filtering should be 3.")

        # Step 7: Locate and click the "Clear all" button to remove filters
        clear_filters_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Clear all')]"))
        )
        clear_filters_button.click()

        # Step 8: Wait and assert that the number of products returns to the original count - 7
        wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Showing 1-7 of 7')]")))
        products_after_clearing = driver.find_elements(By.CSS_SELECTOR, ".products .js-product")
        self.assertEqual(len(products_after_clearing), 7, "Product count after clearing filters should be 7.")

if __name__ == "__main__":
    unittest.main()