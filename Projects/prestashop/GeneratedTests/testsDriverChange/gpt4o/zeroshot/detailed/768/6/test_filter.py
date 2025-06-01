import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open the home page - Already done in setUp
        
        # Step 2: Click on the "Art" category in the top menu
        art_category_link = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ul[@id='top-menu']//li//a[@class='dropdown-item' and text()=' Art ']")))
        art_category_link.click()
        
        # Step 3: Wait for the category page to load
        wait.until(EC.presence_of_element_located((By.ID, "category")))

        # Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        composition_filter = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//section[@id='search_filters']//p[text()='Composition']/..//a[contains(text(), 'Matt paper')]")))
        composition_filter.click()

        # Step 5: Wait for the filter to apply
        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']//article")) == 3)

        # Step 7: Assert that the number of product tiles is reduced from 7 to 3
        products_after_filter = driver.find_elements(By.XPATH, "//div[@id='js-product-list']//article")
        if not products_after_filter or len(products_after_filter) != 3:
            self.fail("Filter did not reduce products to 3 as expected")

        # Step 8: Locate and click the "Clear all" button to remove filters
        clear_all_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(@class, 'clear-all-filters')]")))  # Adjust selector based on real button
        clear_all_button.click()

        # Step 9: Wait and assert that the number of products returns to the original count - 7
        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']//article")) == 7)
        products_after_clear = driver.find_elements(By.XPATH, "//div[@id='js-product-list']//article")
        if not products_after_clear or len(products_after_clear) != 7:
            self.fail("Filter clearing did not reset products to 7 as expected")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()