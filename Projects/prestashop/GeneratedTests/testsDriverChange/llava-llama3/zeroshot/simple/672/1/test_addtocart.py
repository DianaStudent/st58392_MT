import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

class TestAddToCartSuccess(unittest.TestCase):

def setUp(self):
self.driver = webdriver.Chrome()
self.driver.get("http://localhost:8080/en/")
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

def test_addtocart(self):

# Find the first product on the page
first_product = self.wait.until(EC.visibility_of_element_located((By.XPATH,
// *[name][contains('Add to Cart')])))

# Select the first product and click 'add'
product_name = first_product.find_element_by_tag_name("h4")
product_name.click()
add_button = self.wait.until(EC.element_to_be_clickable(
// *[text][contains('Add to Cart')]))

add_button.click()

# Wait for the modal confirmation to appear
modal_title = self.wait.until(EC.text_to_be(
// *[contains('Product successfully added')])))

self.assertEqual(modal_title, "Product successfully added")

if __name__ == "__main__":
unittest.main()
This test uses the following imports:

* `unittest`: The built-in Python unit testing framework.
* `selenium.webdriver`: Selenium WebDriver for controlling a web browser.
* `keys`: Selenium Key interface to simulate key presses.
* `ui`: Selenium WebDriver UI interface.

The test defines three methods: `setUp`, `tearDown`, and `test_addtocart`.

The `setUp` method initializes the web browser, navigating to the homepage of the website mentioned in the task description. It also defines a `wait` variable that is used throughout the test for explicit wait times.

The `tearDown` method is called after each test case has completed. In this test, it simply calls the `driver.quit()` method of the WebDriver instance to close the web browser.

The `test_addtocart` method first finds the first product on the page using an XPath expression that selects elements with a `name` attribute containing "Add to Cart". It then selects and clicks on the first product to add it to the cart. The test then waits for a modal confirmation window to appear with the title "Product successfully added" and fails the test if this is not present.

This test will pass only if a product can be successfully added to the cart and the modal confirmation is displayed correctly.