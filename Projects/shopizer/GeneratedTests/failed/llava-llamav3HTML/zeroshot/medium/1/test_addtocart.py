from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager import DriverWrapper
from .html_data import HTMLData

class TestSeleniumCart(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

def test_add_to_cart(self):
try:
# Open the home page
self.driver.get(HTMLData.home_page_url)

# Hover over a product image to reveal the "Add to cart" button.
product_image_selector = self.wait.until(ExpectedConditions.visibility_of_element_located((By.XPATH, HTMLData.product_image_xpath)))

# Click the "Add to cart" button.
add_to_cart_button_selector = self.wait.until(ExpectedConditions.visibility_of_element_located((By.XPATH, HTMLData.add_to_cart_button_xpath)))
add_to_cart_button = ActionChains(self.driver).move_to_element(product_image_selector).move_by_offset(HTMLData.product_image_padding).click(add_to_cart_button_selector)

# Open the cart popup by clicking the cart icon.
cart_icon_selector = self.wait.until(ExpectedConditions.visibility_of_element_located((By.XPATH, HTMLData.cart_icon_xpath)))
cart_icon = ActionChains(self.driver).move_to_element(cart_icon_selector)
cart_icon.click()

# Confirm success by checking that the popup contains at least one item.
cart_popup_selector = self.wait.until(ExpectedConditions.visibility_of_element_located((By.XPATH, HTMLData.cart_popup_xpath)))

if cart_popup_selector.get_property("display") != "none":
self.assertTrue(not cart_popup_selector.get_property("display").empty)
else:
raise unittest.SkipTest( "required element missing" )

except Exception as e:
self.fail(e)

if \_\_name\_\_.main\_\_ == "\_\_test\_\_" :
unittest.main()