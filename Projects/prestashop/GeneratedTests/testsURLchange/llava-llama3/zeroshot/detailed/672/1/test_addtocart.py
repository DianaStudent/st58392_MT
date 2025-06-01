import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class EcommerceTest(unittest.TestCase):
@classmethod
def setUpClass(cls):
cls.driver = webdriver.Chrome()
 cls.driver.maximize_window()

@classmethod
def tearDownClass(cls):
cls.driver.quit()

def test_addtocart(self):
self.driver.get("http://localhost:8080/en/")
select = Select(self.driver.find_element_by_name("category"))
select.select_by_value("ART")
product_list = WebDriverWait(self.driver, 20).until(
presence_of_element_located((By.XPATH, "//a[contains(text(), 'The best is yet to come')]")))
for product in product_list:
if self.product_details(product):
self.driver.execute_script(f"arguments[0].click() ;")
break
self.assertTrue(self.product_added_to_cart())

def product_details(product):
product_name = product.find_element_by_tag_name("span").text.strip()
return product_name

def product_added_to_cart():
modal_title = WebDriverWait(self.driver, 20).until(
presence_of_element_located((By.XPATH,
f"//div[contains(@class,'modal')] and contains(text(), 'successfully added')")))
return modal_title is not None

if __name__ == "__main__":
unittest.main()
This code defines an EcommerceTest class that extends unittest.TestCase. The setUpClass method sets up a WebDriver instance with the Chrome browser before running any test methods.

The tearDownClass method terminates the WebDriver instance after all tests have been completed.

The test\_addtocart method uses the driver object to navigate to the home page of the e-commerce website, then selects a product category from the top navigation menu using a select element. It waits for the category page to load and then clicks on the first product in the list. The product\_details function is called with the selected product as an argument to check if it's added to the cart successfully.

The product\_added\_to\_cart function waits for a modal popup to appear after adding a product to the cart, and then checks the presence of a 'modal' class element with text that includes 'successfully added'.

Note: The code above assumes that the website has unique element names or attributes that can be used as locators for Selenium's find\_element method.