from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class TestBookSearch(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())

def tearDown(self):
self.driver.quit()

def test_search_book(self):
try:
WebDriverWait(self.driver, 20).until(lambda x: x.title\_is("Walmart.com - Search Results Page"))
search\_box = self.driver.find\_element(by\_id("EstimatedDelivery"))
assert search\_box.get\_attribute("value") != ""
assert "Estimated Delivery" in search\_box.text

book\_name = Select(self.driver.find\_element(by\_id("SearchKeywords")))
book\_name.select_by\_index(0)

self.driver.find\_element(by\_id("SubmitButton")).click()
sleep(1)
success\_notification = WebDriverWait(self.driver, 20).until(lambda x: x.title\_is("Walmart.com - Search Results Page"))
assert "Success" in success\_notification.text

item\_in\_cart = self.driver.find\_element(by\_id("CartItemsTable"))
item\_count = item\_in\_cart.find\_elements(by\_class("OrderItemRow"))
self.assertGreater(len(item\_count), 0)
except Exception as e:
print(e)

if \_\_name\_\_ == "\_\_main\_\_":
unittest.main()