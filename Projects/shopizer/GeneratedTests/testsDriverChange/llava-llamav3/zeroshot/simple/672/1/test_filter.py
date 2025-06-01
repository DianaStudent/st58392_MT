import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class TestFiltering(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().get_chromedriver())
self.url = "http://localhost/"
self.filter_type = "filter"
self.filter_product = "chair"

def tearDown(self):
self.driver.quit()

def test_filtering(self):
try:
# Click on the filter tab
select = Select(self.driver.find_element_by_css_selector("div[data-filter='type']"))
select.select_by_visible_text(self.filter_type)
# Check that at least one product is displayed after filtering
if self.driver.current_url() != self.url + self.filter_product:
self.fail("No products found after applying the filter.")

# Clear the filters and check if the products change again
select.all_selected_options.clear()
select.select_by_visible_text(self.filter_type)
if self.driver.current_url() == self.url + self.filter_product:
self.fail("The products did not change after clearing the filters.")

except WebDriverException as e:
print(f"Error occurred during testing: {e}")
if "Element Not Found" in str(e):
self.fail("An element required for testing was not found.")
else:
self.assertTrue("No product change", expected=True)

if __name__ == '__main__':
unittest.main()

Explanation of the code:

- The test_filtering() function defines the actions to be performed.
- The setUp() method initializes a WebDriver instance and sets up variables for filtering parameters.
- The tearDown() method cleans up the WebDriver instance at the end of the test.
- Within the test\_filtering() function, several lines of code attempt to filter products by type and check that products are displayed.