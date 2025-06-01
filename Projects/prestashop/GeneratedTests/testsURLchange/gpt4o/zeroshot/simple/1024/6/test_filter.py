import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_process(self):
        driver = self.driver

        # Wait for the "Art" category link and navigate to it
        art_category_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Art']")))
        art_category_link.click()

        # Wait for the filter sidebar
        filter_sidebar = self.wait.until(EC.presence_of_element_located((By.ID, "search_filters")))

        # Locate and check the "Matt paper" checkbox
        matt_paper_checkbox = filter_sidebar.find_element(By.XPATH, "//label[contains(.//a, 'Matt paper')]//input[@type='checkbox']")
        matt_paper_checkbox.click()

        # Wait and check that the number of visible products has been updated
        products_list = self.wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))
        products = products_list.find_elements(By.CLASS_NAME, "product-miniature")
        filtered_product_count = len(products)

        # Validate that the product count changes
        self.assertNotEqual(filtered_product_count, 7, "The product count should change after applying filter.")

        # Uncheck the "Matt paper" checkbox to clear the filter
        matt_paper_checkbox.click()

        # Wait and check that the number of visible products has returned to original
        products_list = self.wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))
        products = products_list.find_elements(By.CLASS_NAME, "product-miniature")
        unfiltered_product_count = len(products)

        # Validate that the product count returns to original
        self.assertEqual(unfiltered_product_count, 7, "The product count should return to original after clearing filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()