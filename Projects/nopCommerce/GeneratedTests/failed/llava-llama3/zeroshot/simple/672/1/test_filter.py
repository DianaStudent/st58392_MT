from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestEptoCommerce(unittest.TestCase):

def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())

def tearDown(self):
self.driver.quit()

def test_search_product_with_price_filter(self):
# Navigate to the website
self.driver.get("http://max/")

# Perform a product search using the query "book"
search_input = self.driver.find_element_by_name("search")
search_input.send_keys("book")
search_input.send_keys(Keys.RETURN)

# Apply a price filter by navigating to a URL that includes the price parameter
price_filter_url = "http://max/?price_min=50&price_max=100"
self.driver.get(price_filter_url)

# Confirm success by checking that the resulting product grid is updated
product_grid = self.driver.find_element_by_css_selector("div.product-grid")

if product_grid.find_elements_by_css_selector("li") != 2:
self.fail("Product grid did not update after applying price filter.")

# Test for required elements on the webpage
required_elements = ["eptoCommerce", "Search", "Local Businesses"]
for element in required_elements:
if self.driver.find_element_by_text(element) is None:
self.fail(f"Element {element} was not found on the webpage.")

if __name__ == "__main__":
unittest.main()
```