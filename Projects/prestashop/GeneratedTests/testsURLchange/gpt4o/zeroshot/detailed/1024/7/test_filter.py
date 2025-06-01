from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_process(self):
        driver = self.driver

        # Step 1: Open the home page is done in setUp()

        # Step 2: Click on the "Art" category in the top menu
        art_category = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '9-art')]"))
        )
        art_category.click()

        # Step 3: Wait for the category page to load
        self.wait.until(
            EC.presence_of_element_located((By.ID, "category"))
        )

        # Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        filter_section = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//section[@class='facet clearfix']//p[text()='Composition']"))
        )
        matt_paper_filter = driver.find_element(
            By.XPATH, "//label[.//a[contains(text(), 'Matt paper')]]//input[@type='checkbox']"
        )
        self.wait.until(EC.element_to_be_clickable(matt_paper_filter)).click()

        # Step 5: Wait for the filter to apply and check product count
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']//article[@class='product-miniature']"))
        )
        filtered_products = driver.find_elements(By.XPATH, "//div[@id='js-product-list']//article[@class='product-miniature']")
        self.assertEqual(len(filtered_products), 3, "The number of products after applying the filter should be 3.")

        # Step 6: Locate and click the "Clear all" button to remove filters
        clear_filter_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Clear all')]"))
        )
        clear_filter_button.click()

        # Step 7: Wait for the number of products to return to original count
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']//article[@class='product-miniature']"))
        )
        all_products = driver.find_elements(By.XPATH, "//div[@id='js-product-list']//article[@class='product-miniature']")
        self.assertEqual(len(all_products), 7, "The number of products after clearing the filter should be 7.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()