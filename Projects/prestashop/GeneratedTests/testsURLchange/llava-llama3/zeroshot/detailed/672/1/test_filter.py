import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class TestSeleniumFiltering(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_filtering(self):
# Step 1: Open the home page.
self.driver.get("http://localhost:8080/en/")
# Step 2: Click on the "Art" category in the top menu.
self.wait_for_element("//*[contains(text(), 'art')]", Keys.RETURN)
# Step 3: Wait for the category page to load.
self.wait_for_element("//*[contains(text(), 'art')]", Keys.RETURN)

# Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition".
filter_section = self.driver.find_element_by_xpath("//*[contains(text(), 'composition')]")
matt_paper_filter = WebDriverWait(filter_section, 20).until(EC.element_located((By.XPATH, "//input[@data-name='matt-paper']"))))

matt_paper_filter.click()

# Step 5: Wait for the filter to apply.
self.wait_for_element("//*[contains(text(), 'art')]", Keys.RETURN)

# Step 6: Locate and click the "Clear all" button to remove filters.
clear_all_button = self.driver.find_element_by_xpath("//*[contains(text(), 'clear all')]")
clear_all_button.click()

# Step 7: Wait for the number of product items to change from 7 to 3.
product_tiles = WebDriverWait(self.driver, 20).until(EC.visibility_of_elements_located((By.XPATH, "//div[@class='masonry-product-list']//a[@data-name]"))))

# Verify that the number of visible product tiles has changed.
self.assertEqual(len(product_tiles), 3)

def wait_for_element(self, xpath: str, timeout: int = None) -> Element:
if timeout is not specified or timeout <= 0:
return self.driver.find_element_by_xpath(xpath)
else:
element = WebDriverWait(self.driver, timeout).until(EC.element_located((By.XPATH, xpath))))
return element

def test_filtering_with_unittest(self):
# Step 1: Open the home page.
self.driver.get("http://localhost:8080/en/")
# Step 2: Click on the "Art" category in the top menu.
self.wait_for_element("//*[contains(text(), 'art')]", Keys.RETURN)
# Step 3: Wait for the category page to load.
self.wait_for_element("//*[contains(text(), 'art')]", Keys.RETURN)

# Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition".
filter_section = self.driver.find_element_by_xpath("//*[contains(text(), 'composition')]")
matt_paper_filter = WebDriverWait(filter_section, 20).until(EC.element_located((By.XPATH, "//input[@data-name='matt-paper']"))))

matt_paper_filter.click()

# Step 5: Wait for the filter to apply.
self.wait_for_element("//*[contains(text(), 'art')]", Keys.RETURN)

# Step 6: Locate and click the "Clear all" button to remove filters.
clear_all_button = self.driver.find_element_by_xpath("//*[contains(text(),'clear all')]")
clear_all_button.click()

# Step 7: Wait for the number of product items to change from 7 to 3.
product_tiles = WebDriverWait(self.driver, 20).until(EC.visibility_of_elements_located((By.XPATH, "//div[@class='masonry-product-list']//a[@data-name]"))))

# Verify that the number of visible product tiles has changed.
self.assertEqual(len(product_tiles), 3)

if name == "main":
unittest.main()