from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class TestFiltering(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_filter_a(self):
# Open the category page.
self.driver.get("http://localhost:3000/category-a")

# Wait until products and filters are fully loaded.
WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
html_data[1]))))

# Locate the "Brand A" checkbox filter using its associated input.
brand_a_checkbox = WebDriverWait(self.driver, 2).until(EC.element_located((By.XPATH,
html_data[3]))))

# Confirm it is checked.
self.assertFalse(brand_a_checkbox.get_attribute("checked") == True)

# Apply and remove the filter.
self.assertTrue(brand_a_checkbox.get_attribute("checked"))
time.sleep(2)
self.assertFalse(brand_a_checkbox.get_attribute("checked") == False)

# Move the right slider handle to reduce the maximum price to 1159.
price_slider = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH,
html_data[4]))))
max_price_input = self.driver.find_element(By.ID,
"priceSliderMax")
new_max_price = "1159"
WebDriverWait(max_price_input, 2).until(
EC.text_to_be(max_price_input, new_max_price))

# Confirm the number of visible product cards changed.
product_cards = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,
html_data[2]))))

self.assertTrue(len(product_cards) < len(initial_product_cards))

def test_filter_b(self):
# Open the category page.
self.driver.get("http://localhost:3000/category-a")

# Wait until products and filters are fully loaded.
WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
html_data[1]))))

# Locate the price slider component and move the right slider handle to reduce the maximum price to 1159 .
price_slider = WebDriverWait(self.driver, 2).until(EC.element_located((By.XPATH,
html_data[4])))
max_price_input = self.driver.find_element(By.ID,
"priceSliderMax")
new_max_price = "1159"
WebDriverWait(max_price_input, 2).until(
EC.text_to_be(max_price_input, new_max_price))

# Confirm the number of visible product cards changed.
product_cards = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,
html_data[2]))))

self.assertTrue(len(product_cards) < len(initial_product_cards))

if __name__ == "__main__":
unittest.main()

Note: You need to install the necessary Selenium and unittest packages by running pip install selenium unittest. Also, you can download ChromeDriver from the official website and place it in your project directory before running this code.