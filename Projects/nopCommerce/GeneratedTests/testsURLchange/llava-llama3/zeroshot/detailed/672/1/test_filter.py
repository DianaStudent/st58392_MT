import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class TestEpcommerceTest(unittest.TestCase):
def setUp(self):
driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
self.driver = driver
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

def test_search_book(self):
# Step 1: Open the home page.
url = "http://max/"
self.wait.until(EC.url_to_be(url))

# Step 2: Click on the search bar and enter "book".
search_bar = self.wait.until(EC.presence_of_element_located((html_data["search_bar"],)))
search_bar.send_keys("book")
search_bar.send_keys(Keys.RETURN)

# Step 3: Confirm that the product grid is updated.
product_grid = self.wait.until(EC.presence_of_element_located((html_data["product_grid"],)))
self.wait.until(EC.visibility_of_all_elements_located(product_grid))

def test_apply_price_filter(self):
url = "http://max/book?min=0&max=25"
self.wait.until(EC.url_to_be(url))
product_grid = self.wait.until(EC.presence_of_element_located((html_data["product_grid"],)))
self.wait.until(EC.visibility_of_all_elements_located(product_grid))

def test_confirm_filter_updates(self):
# Step 4: Locate and interact with the price range slider
price_range_slider = self.wait.until(EC.presence_of_element_located((html_data["price_range_slider"],)))
ActionChains(self.driver).drag_by(price_range_slider, "100").perform()
product_grid = self.wait.until(EC.presence_of_element_located((html_data["product_grid"],)))
self.wait.until(EC.visibility_of_all_elements_located(product_grid))

if __name__ == '__main__':
unittest.main()

Note: This test script uses the html\_data variable to generate selectors for interacting with elements on the UI. The html\_data variable should be defined in a separate file and imported into this script before running the tests.

Also, note that this test is only an example and may require modification to accurately test the specific functionalities of the given website.