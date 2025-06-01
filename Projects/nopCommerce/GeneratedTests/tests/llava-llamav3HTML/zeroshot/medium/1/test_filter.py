import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager import ChromeDriverManager

class TestBookSearch(unittest.TestCase):

def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().install())

def tearDown(self):
self.driver.quit()

def test_book_search(self):
# 1. Open the homepage.
self.driver.get('https://www.example.com')

# 2. Click on the "Search" link from the top navigation.
search_link = self.wait_for_elementLocated(By.XPATH,
'//a[contains(text(), "Search")]')
search_link.click()

# 3. Enter the search term and perform the search.
search_field = self.wait_for_elementLocated(
By.XPATH, "//input[contains(@name, 'query')]")
search_field.send_keys('book')
search_button = self.wait_for_elementLocated(
By.XPATH, "//button[contains(text(), 'Search')]")

search_button.click()

# 4. Locate and interact with the price range slider.
price_range = self.wait_for_elementLocated(
By.XPATH, "//div[contains(@class, 'price-range')]")
slider = WebDriverWait(self.driver, 20).until(
lambda x: x.find_element(By.XPATH,
'//div[contains(@class, "price-range")]'))
price_range_max = self.wait_for_elementLocated(
By.XPATH, "//span[contains(text(), 'Max Price')]")

# Test if the price range maximum value is visible
if not price_range_max.is_displayed():
self.fail('Price Range Maximum Value is not Visible')

if self.price_range_max_value > 100:
# Update the query parameter to include the price filter.
url = self.driver.current_url()
new_url = url + f'?price_min={100}&price_max={500}'
self.wait_for_elementLocated(By.XPATH,
f'//a[contains(@href, "{new_url}")]')

# 5. Wait for the page to update and verify that:
#    - The filtered URL includes the price parameter.
#    - The product list is changed

# Test if the query parameter including the price filter
# exists in the URL
if 'price_min' not in self.url or 'price_max' not in self.url:
self.fail('Price Filter Query Parameter Not Visible')

# Test if the product grid is updated
product_grid = self.wait_for_elementLocated(
By.XPATH, "//div[contains(@class, 'product-grid')]")
if len(product_grid) == 0:
self.fail('Product Grid Is Empty')

def wait_for_elementLocated(self, by, xpath):
driver = WebDriverWait(self.driver, 20)
return driver.until(by, lambda x: x.find_element(by.xpath(xpath)))

if __name__ == '__main__':
unittest.main()