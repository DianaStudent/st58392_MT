import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from html_data import HtmlData

class TestProductSearch(unittest.TestCase):
def setUp(self):
# Initialize the driver with ChromeDriver
self.driver = webdriver.Chrome()

def tearDown(self):
# Close the browser window after test execution
self.driver.quit()

def test_product_search(self):
# Perform a product search using the query "book"
search_box = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, HtmlData.SEARCH_BOX)))
search_box.send_keys("book")
search_box.send_keys(Keys.RETURN)

# Check if the grid is updated
product_grid = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, HtmlData.PRODUCT_GRID)))

if len(product_grid) == 0:
self.fail("Product grid is empty")

def test_filter_by_price(self):
# Navigate to a URL that includes the price parameter
price_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, HtmlData.PRICE_INPUT)))
price_input.clear()
price_input.send_keys("25.00")
price_input.send_keys(Keys.RETURN)

if not self.driver.current_url().startswith(HtmlData.PRODUCT_LIST_URL):
self.fail("Current URL does not start with 'product_list_url'")

# Check if the price is updated
price_text = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, HtmlData.PRICE_TEXT)))
if "25.00" != price_text:
self.fail("Price text is incorrect")

def test_product_search_and_filter_by_price(self):
# Call test_product_search method to perform a search
test_product_search()

# Call test_filter_by_price method to filter by price
test_filter_by_price()

if __name__ == '__main__':
unittest.main()