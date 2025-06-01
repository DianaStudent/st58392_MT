import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_product_filter_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click on the "Art" category in the top menu.
        art_category_link = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[contains(@href, '/9-art')]")
        ))
        art_category_link.click()

        # Step 2: Wait for the category page to load.
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h1[text()='Art']")
        ))

        # Step 3: Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        composition_filter = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[span[contains(text(), 'Matt paper')]]/span/input")
        ))
        composition_filter.click()

        # Step 4: Wait for the filter to apply.
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#js-product-list .product-miniature")
        ))

        # Step 5: Assert that the number of product tiles is reduced from 7 to 3.
        filtered_products = driver.find_elements(By.CSS_SELECTOR, "#js-product-list .product-miniature")
        if not filtered_products or len(filtered_products) != 3:
            self.fail("Filtered products do not match expected count of 3")

        # Step 6: Locate and click the "Clear all" button to remove filters.
        clear_all_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[text()='Clear all']")
        ))
        clear_all_button.click()

        # Step 7: Wait and assert that the number of products returns to original count - 7.
        wait.until(EC.number_of_elements_to_be((By.CSS_SELECTOR, "#js-product-list .product-miniature"), 7))
        final_products = driver.find_elements(By.CSS_SELECTOR, "#js-product-list .product-miniature")
        if not final_products or len(final_products) != 7:
            self.fail("Final product count does not match expected count of 7 after clearing filters")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()