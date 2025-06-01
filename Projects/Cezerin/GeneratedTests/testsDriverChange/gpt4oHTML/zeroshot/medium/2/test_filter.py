import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryFilter(unittest.TestCase):

    def setUp(self):
        # Set up ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("data:text/html," + self.create_initial_html())
    
    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()
    
    def create_initial_html(self):
        # This is a shortened version to simulate the HTML data
        return "<body style=\"margin-top: 131px; zoom: 50%;\">" + \
               "<div id=\"app\"><header>...</header><section class=\"section section-category\">" + \
               "<div class=\"container\"><div class=\"columns\">" + \
               "<div class=\"column is-one-quarter left-sidebar\">" + \
               "<div class=\"attribute-filter\">" + \
               "<div class=\"attribute\"><div class=\"attribute-title\">Brand</div>" + \
               "<label><input type=\"checkbox\"/>Brand A</label>" + \
               "<label><input type=\"checkbox\"/>Brand B</label></div></div>" + \
               "</div><div class=\"column\">" + \
               "<div class=\"columns is-multiline is-mobile products\">" + \
               "<div class=\"column\" style=\"height:280px;\"><a href=\"/category-a/product-a\"><div class=\"content product-caption\">" + \
               "<div class=\"product-name\">Product A</div></div></a></div>" + \
               "<div class=\"column\" style=\"height:280px;\"><a href=\"/category-a/product-b\"><div class=\"content product-caption\">" + \
               "<div class=\"product-name\">Product B</div></div></a></div>" + \
               "</div></div></div></div></section></div></body>"
    
    def test_filter_brand_a(self):
        driver = self.driver
        
        # Wait until the category page is fully loaded
        wait = WebDriverWait(driver, 20)
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column")))
        
        initial_product_count = len(products)
        
        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[input/@type='checkbox' and contains(., 'Brand A')]")))
        checkbox = brand_a_checkbox_label.find_element(By.TAG_NAME, 'input')
        
        self.assertTrue(checkbox, "Brand A checkbox is missing")
        
        # Click to select Brand A
        checkbox.click()
        
        time.sleep(2)  # Wait for UI to update
        
        # Verify the number of displayed product cards changes
        products = driver.find_elements(By.CSS_SELECTOR, ".products .column")
        updated_product_count = len(products)
        
        self.assertNotEqual(initial_product_count, updated_product_count, "Product count did not change after applying Brand A filter")
        
        # Uncheck the "Brand A" filter
        checkbox.click()
        
        time.sleep(2)  # Wait for UI to update back
        
        # Verify the original number of product cards is restored
        products = driver.find_elements(By.CSS_SELECTOR, ".products .column")
        final_product_count = len(products)
        
        self.assertEqual(initial_product_count, final_product_count, "Product count did not restore after removing Brand A filter")
        
        # Locate the price slider component and simulate interaction
        # For demonstration, we will use a different approach since there's no explicit price slider in the provided code
        handle = driver.find_element(By.CSS_SELECTOR, ".price-filter-values .column.has-text-left")
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(handle, 5, 0).perform()
        
        time.sleep(2)  # Wait for UI to update
        
        # Verify product count changes again
        products = driver.find_elements(By.CSS_SELECTOR, ".products .column")
        after_price_filter_count = len(products)
        
        self.assertNotEqual(final_product_count, after_price_filter_count, "Product count did not change after applying price filter")

if __name__ == "__main__":
    unittest.main()