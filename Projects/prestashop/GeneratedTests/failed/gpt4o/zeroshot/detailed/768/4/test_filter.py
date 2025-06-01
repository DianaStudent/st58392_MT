from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open home page
        # (Already opened in setUp)

        # Step 2: Click on the "Art" category in the top menu
        art_category = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[text()='Art']")))
        art_category.click()

        # Step 3: Wait for the category page to load
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h1[text()='Art']")))

        # Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        composition_filter = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[contains(., 'Matt paper')]//input[@type='checkbox']")))
        composition_filter.click()

        # Step 5: Wait for the filter to apply
        wait.until(lambda driver: len(driver.find_elements(
            By.CSS_SELECTOR, ".js-product")) == 3)

        # Step 6: Assert the number of product tiles is reduced to 3
        products = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".js-product")))
        self.assertEqual(len(products), 3)

        # Step 7: Locate and click the "Clear all" button to remove filters
        clear_all_btn = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[text()='Clear all']")))
        clear_all_btn.click()

        # Step 8: Wait and assert that the number of products returns to 7
        wait.until(lambda driver: len(driver.find_elements(
            By.CSS_SELECTOR, ".js-product")) == 7)
        products_after_clear = driver.find_elements(
            By.CSS_SELECTOR, ".js-product")
        self.assertEqual(len(products_after_clear), 7)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()