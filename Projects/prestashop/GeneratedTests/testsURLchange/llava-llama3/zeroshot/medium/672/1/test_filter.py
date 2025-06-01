import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class FilterTest(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().get_chromedriver())
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

def test_filter(self):
# Step 1: Open the home page
self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(''))"), "[data-name*='home']")))
self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(''))), "[data-name*='home']")))
# Step 2: Navigate to a product category
self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(''))), "[data-name*='product-category']")))
self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(''))), "[data-name*='product-category']")))
# Step 3: Verify that the filter sidebar is present
self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(''))), "[data-name*='filter-sidebar']")))
self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(''))), "[data-name*='filter-sidebar']")))
# Step 4: Select the filter using label-based selection
filter_checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text('Filter')))]"))
filter_checkbox.click()
self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text('Filter')))]")))
# Step 5: Verify that the number of visible product items changes
product_count = self.wait.until(EC.number_of_elements_located((By.XPATH, "*[data-name*='product-list']")))
assert(product_count != initial_product_count)
# Step 6: Clear all filters
self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text('Clear All Filters')))]")))
clear_all_filter = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text('Clear All Filters')))]")))
clear_all_filter.click()
# Step 7: Verify that the number of products returns to the original count
product_count = self.wait.until(EC.number_of_elements_located((By.XPATH, "*[data-name*='product-list']")))
assert(product_count == initial_product_count)

if __name__ == '__main__':
unittest.main()