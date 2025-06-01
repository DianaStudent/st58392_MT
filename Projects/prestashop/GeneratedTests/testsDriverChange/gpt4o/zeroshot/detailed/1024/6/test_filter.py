import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def test_product_filter_by_composition(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page and click on the "Art" category in the top menu.
        art_category = wait.until(
            EC.presence_of_element_located((By.XPATH, "//ul[@id='top-menu']//a[contains(@href, '9-art')]"))
        )
        art_category.click()

        # Step 2: Wait for the category page to load and apply the "Matt paper" filter under "Composition".
        composition_filter = wait.until(
            EC.presence_of_element_located((By.XPATH, "//section[@data-name='Composition']//a[text()=' Matt paper ']"))
        )
        composition_filter.click()

        # Step 3: Wait for the filter to apply and assert that the number of products is reduced from 7 to 3.
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']//div[@class='products row']/div[3]"))
        )
        product_tiles_after_filter = driver.find_elements(By.XPATH, "//div[@id='js-product-list']//div[@class='products row']/div")
        
        if not product_tiles_after_filter:
            self.fail("No product tiles found after applying filters.")
        
        self.assertEqual(len(product_tiles_after_filter), 3, "Product count after filter application is incorrect.")

        # Step 4: Locate and click the "Clear all" button to remove filters.
        clear_filters_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Clear all']"))
        )
        clear_filters_button.click()

        # Step 5: Wait and assert that the number of products returns to the original count of 7.
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']//div[@class='products row']/div[7]"))
        )
        product_tiles_after_clearing_filter = driver.find_elements(By.XPATH, "//div[@id='js-product-list']//div[@class='products row']/div")
        
        if not product_tiles_after_clearing_filter:
            self.fail("No product tiles found after clearing filters.")
        
        self.assertEqual(len(product_tiles_after_clearing_filter), 7, "Product count after clearing filters is incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()