from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_product(self):
        driver = self.driver
        wait = self.wait

        # Click on the "Art" category in the top menu.
        art_category = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
        )
        art_category.click()

        # Wait for the category page to load.
        filter_section = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='search_filters']"))
        )

        # Locate the filter and apply "Matt paper" under "Composition".
        matt_paper_filter = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//label[@for='facet_input_57074_0']"))
        )
        matt_paper_filter.click()

        # Wait for the filter to apply.
        wait.until(lambda driver: 
            len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div")) == 3)

        # Get product tiles and assert the number is reduced from 7 to 3.
        product_tiles_after_filter = driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div")
        self.assertEqual(len(product_tiles_after_filter), 3, "Filter did not reduce products to 3.")

        # Locate and clear the filter.
        clear_filters_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//section[@id='js-active-search-filters']/following-sibling::button"))
        )
        clear_filters_button.click()

        # Wait for the products to reset to 7.
        wait.until(lambda driver: 
            len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div")) == 7)

        product_tiles_after_clear = driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div")
        self.assertEqual(len(product_tiles_after_clear), 7, "Clear filter did not reset products to 7.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()