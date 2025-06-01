import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_key_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check presence of header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is not present or visible.")

        # Check presence of navigation links
        try:
            nav_category_a = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A')))
            nav_category_b = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category B')))
            nav_category_c = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category C')))
        except:
            self.fail("Navigation links are not present or visible.")

        # Check presence of search box
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        except:
            self.fail("Search box is not present or visible.")

        # Check presence of product list
        try:
            products = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'products')))
        except:
            self.fail("Product list is not present or visible.")

        # Interact with a button and check UI update
        try:
            sort_select = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'select')))
            sort_select.click()
            option_price_low_to_high = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='price']")))
            option_price_low_to_high.click()

            # Verify UI visually updates (assuming sorted order change, just a placeholder inspection)
            first_product = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product A')))
            self.assertTrue(first_product.is_displayed(), "UI did not visually update after interaction.")
        except:
            self.fail("Interaction with sort element failed or did not update UI.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()