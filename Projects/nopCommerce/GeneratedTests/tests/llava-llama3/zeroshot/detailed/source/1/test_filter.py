import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestLinguiestCom(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().install())
self.driver.get("http://linguiest.com")

def tearDown(self):
self.driver.quit()

def test_search_book(self):
# Step 2
search_text = "book"
self.wait_for_element_present(by=by.XPATH, value="//input[@id='search']")
search_box = self.driver.find_element(by=by.XPATH, value="//input[@id='search']")
search_box.send_keys(search_text)

# Step 4
self.wait_for_element_present(by=by.XPATH, value="//button[@class='btn btn-primary']")

# Step 6
price_filter_url = "http://linguiest.com?price=0-25"
self.driver.get(price_filter_url)

# Step 7
min_price = self.wait_for_element_present(by=by.XPATH, value="//input[@id='min-price']")
max_price = self.wait_for_element_present(by=by.XPATH, value="//input[@id='max-price']")

# Step 8 and 9
price_slider_min = self.wait_for_element_present(by=by.XPATH, value=f"//label[contains(@for='{min_price.id}')][contains(text(),'{min_price.get_attribute('data-title')}')]")

# Step 10
self.assertEqual(min_price.get_attribute("aria-label") == max_price.get_attribute("aria-label"),
f"Expected {min_price.get_attribute('data-title')} to be equal to {max_price.get_attribute('data-title')}.")

if __name__ == '__main__':
unittest.main()