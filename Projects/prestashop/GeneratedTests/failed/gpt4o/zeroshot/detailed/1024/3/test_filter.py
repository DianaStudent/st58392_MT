from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        driver.get("http://localhost:8080/en/")

        # Step 2: Click on the "Art" category in the top menu
        art_category_selector = "//ul[@id='top-menu']//a[contains(text(), 'Art')]"
        art_category = wait.until(EC.presence_of_element_located((By.XPATH, art_category_selector)))
        art_category.click()

        # Step 3: Wait for the category page to load
        product_list_selector = "//h1[contains(text(), 'Art')]"
        wait.until(EC.presence_of_element_located((By.XPATH, product_list_selector)))

        # Step 4: Locate and apply the "Matt paper" checkbox filter under "Composition"
        filter_section_selector = "//section[contains(@class, 'facet')]//a[contains(text(), 'Matt paper')]"
        filter_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, filter_section_selector)))
        filter_checkbox.click()

        # Step 5: Wait for the filter to apply
        reduced_product_count_selector = "//div[@id='js-product-list']//div[contains(@class, 'product-miniature')]"
        products_filtered = wait.until(EC.presence_of_all_elements_located((By.XPATH, reduced_product_count_selector)))
        self.assertEqual(len(products_filtered), 3, "Product count after applying filter is not 3")

        # Step 6: Locate and click the "Clear all" button to remove filters
        clear_filter_selector = "//button[contains(@class, 'js-search-toggler')]"
        clear_filter_button = wait.until(EC.element_to_be_clickable((By.XPATH, clear_filter_selector)))
        clear_filter_button.click()

        # Step 7: Wait and assert that the number of products returns to the original count
        products_original = wait.until(EC.presence_of_all_elements_located((By.XPATH, reduced_product_count_selector)))
        self.assertEqual(len(products_original), 7, "Product count after clearing filters is not 7")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()