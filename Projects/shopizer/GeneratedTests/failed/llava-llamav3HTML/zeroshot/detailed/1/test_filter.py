from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def setUp(self):
self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class TestEcomScenario(unittest.TestCase):

def test_ecom_scenario(self):
# Step 1: Open the home page.
self.driver.get("http://localhost/")

# Step 2: Apply the "Tables" filter by clicking the corresponding tab.
tables_tab = self.wait_for_element_located((By.XPATH, "//li[@class='tabs-item']//a[contains(text(),'Tables')]"))
tables_tab.click()

# Step 3: Wait for product grid to update.
self.product_grid = self.wait_for_product_grid_update()
print(f"Product count before filter application: {len(self.product_grid)}")

# Step 4: Store number of visible products (1 product).
visible_products = len(self.product_grid)

# Step 5: Switch to the "Chairs" filter and wait for grid to refresh.
chairs_tab = self.wait_for_element_located((By.XPATH, "//li[@class='tabs-item']//a[contains(text(),'Chairs')]"))
chairs_tab.click()

self.chairs_grid = self.wait_for_product_grid_update()
print(f"Product count after 'Chairs' filter application: {len(self.chairs_grid)}")

# Step 6: Verify that the list of products is updated and different from the previous.
self.assertEqual(len(self.product_grid), len(self.chairs_grid))
self.assertNotEqual(set(self.product_grid), set(self.chairs_grid))

# Step 7: Then click the "All" filter to reset (4 products).
all_tab = self.wait_for_element_located((By.XPATH, "//li[@class='tabs-item']//a[contains(text(),'All')]"))
all_tab.click()

self.all_products = self.wait_for_product_grid_update()
print(f"Product count after 'All' filter application: {len(self.all_products)}")

# Step 8: Confirm that product list contains more items than after previous filters.
self.assertGreater(len(self.all_products), visible_products)

def tearDown(self):
self.driver.quit()

if __name__ == '__main__':
unittest.main()