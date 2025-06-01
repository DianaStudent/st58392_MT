import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

class TestCategoryPage(unittest.TestCase):
def setUp(self):
self.driver = ChromeDriverManager().create_binary()

def tearDown(self):
self.driver.quit()

def test_category_page(self):
try:
# Open the category page.
category_page_url = 'http://localhost:3000/category-a'
self.driver.get(category_page_url)
# Locate and apply the "Brand A" checkbox filter.
brand_a_filter_checkbox = self.wait_for_element_located((By.XPATH, "//input[contains(@name, 'brand-a')]"))
self.driver.execute_script(f'arguments[0].click();', brand_a_filter_checkbox)

wait = WebDriverWait(self.driver, 20)
# Verify that the number of displayed product cards changes (e.g. 2 → 1).
product_cards_count = self.wait_for_element_located((By.XPATH,
'\*//*[contains(@class, "product-card")][1]')
current_product_cards_count = int(product_cards_count.text)

original_product_cards_count = self.wait_for_element_located((By.XPATH,
'\*//*[contains(@class, "product-card")][1]')
prev_product_cards_count = int(original_product_cards_count.text)

assert current_product_cards_count != prev_product_cards_count

# Uncheck the "Brand A" filter.
brand_a_filter_checkbox = self.wait_for_element_located((By.XPATH, "//input[contains(@name, 'brand-a')]"))
self.driver.execute_script(f'arguments[0].click();', brand_a_filter_checkbox)

wait = WebDriverWait(self.driver, 20)
current_product_cards_count = int(product_cards_count.text)

assert current_product_cards_count == prev_product_cards_count

# Locate the price slider component.
price_slider = self.wait_for_element_located((By.XPATH, "//input[contains(@id, 'price-range)]'")

# Move one of the slider handles to apply a price range filter.
price_slider.send_keys(Keys.UP)

wait = WebDriverWait(self.driver, 20)
current_product_cards_count = int(product_cards_count.text)

assert current_product_cards_count != prev_product_cards_count

else:
self.fail("Test failed")

if __name__ == '__main__':
unittest.main()