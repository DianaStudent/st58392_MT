from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class ClothingStoreTest(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())

def tearDown(self):
self.driver.quit()

def test_filter_application(self):
# Open the home page
self.driver.get('http://localhost:8080/en/')

# Navigate to a product category
category_page = self.driver.find_element_by_tag_name('div')
while category_page.tag_name != 'li':
category_page = category_page.find_elements_by_tag_name('a')[0].click()

# Select the filter using label-based selection
filter_sidebar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
'//body[contains(@data-name="new-arrivals")]')))
for option in filter_sidebar.find_elements_by_tag_name('label'):
if option.text == 'New Arrivals':
option.click()
break

# Verify that the number of visible product items changes
product_count = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
'//body[contains(@data-name="new-arrivals")]')))

assert product_count > len(categories.find_elements_by_tag_name('li'))

# Clear all filters
for filter in filter_sidebar.find_elements_by_tag_name('label'):
filter.click()
product_count = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
'//body[contains(@data-name="new-arrivals")]')))

assert product_count == len(categories.find_elements_by_tag_name('li'))

if __name__ == '__main__':
unittest.main()