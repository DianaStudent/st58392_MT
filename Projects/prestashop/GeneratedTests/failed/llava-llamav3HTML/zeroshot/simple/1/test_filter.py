from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):
def setUp(self):
driver = ChromeDriverManager().create_instance()
self.driver = driver
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

def test_select_filter_by_label_text(self):
# Wait for the filter sidebar
filter_sidebar = self.wait.until(
Select(by='label').until(ExpectedConditions.visibilityOfElementLocated(by=By.XPATH,'//div[@data-name="dimension-40x60cm"]')))

# Select a checkbox filter by its label text
filter_text = 'mountain fox - vector graphics'
select_filter = self.wait.until(Select(by='label').until(ExpectedConditions.visibilityOfElementLocated(by=By.XPATH, f'//span[@id="product-filter-{filter_text}"]/parent::*'))
select_filter.click()

# Verify that the number of visible product items changes
initial_product_count = len(self.driver.find_elements(By.XPATH, "//a[contains(@href,'http://localhost/en/home-accessories/15-pack-mug-framed-poster.html')]"))
final_product_count = len(self.driver.find_elements(By.XPATH, "//a[contains(@href,'http://localhost/en/home-accessories/15-pack-mug-framed-poster.html')]"))

self.assertEqual(initial_product_count + 1, final_product_count)

# Select a checkbox filter by its label text
select_filter = self.wait.until(Select(by='label').until(ExpectedConditions.visibilityOfElementLocated(by=By.XPATH, f'//span[@id="product-filter-{filter_text}"]/parent::*'))
select_filter.click()

# Verify that the number of visible product items changes
initial_product_count = len(self.driver.find_elements(By.XPATH, "//a[contains(@href,'http://localhost/en/home-accessories/15-pack-mug-framed-poster.html')]"))
final_product_count = len(self.driver.find_elements(By.XPATH, "//a[contains(@href,'http://localhost/en/home-accessories/15-pack-mug-framed-poster.html')]"))

self.assertEqual(initial_product_count - 1, final_product_count)

if any(required_element is missing):
raise ValueError(f'Required element {required_element} not found')

return True

if \_\_name\_\_\_== '\_\_test\_\_':
suite = unittest.TestSuite()
suite.addTest(TestProductFilter)
result = suite.run(result=unittest.TextTestRunner.REPORT_OUTPUT, output_file='output.txt')
print(result)