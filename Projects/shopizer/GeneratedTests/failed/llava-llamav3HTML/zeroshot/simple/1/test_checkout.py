from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(unittest.TestCase):
def setUp(self):
# Set up the environment, like setting up a web driver and other necessary resources.
self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
# Tear down the environment
self.driver.quit()

def test_login(self):
try:
# Check if the website is accessible
self.assertTrue(self.wait.until(self.page_loaded("body")))

# Locate email and password input fields using their ids
email_field = self.wait.until(
self.by.ID("email"))
password_field = self.wait.until(
self.by.ID("password"))

# Enter login credentials for test22@user.com and test**11
email_field.send_keys("test22@user.com")
password_field.send_keys("test**11")

# Click the "Login" button using the id of its parent element
login_button = self.wait.until(self.by.XPATH("//*[contains('class','btn-login')]/parent::*"))
login_button.click()

# Wait for the login to complete before interacting with the rest of the UI.
self.wait.until(self.page_loaded("body"))

# Check if a "Proceed to Checkout" button is present
proceed_button = self.wait.until(
self.by.XPATH("//*[contains('text','Proceed to')]/parent::*"))
proceed_button.click()

# Fill in billing information for test22@user.com and default store
billing_address_field = self.wait.until(
self.by.ID("billing-address"))
billing_address_field.send_keys("1234 Street address My city, QC,CA  <br/> H2H-2H2")
city_field = self.wait.until(self.by.ID("city"))
city_field.send_keys("Default store")
state_field = self.wait.until(self.by.ID("state"))
select_city_state(Select(state_field))
zip_code_field = self.wait.until(self.by.ID("zip-code"))
zip_code_field.send_keys("12345")

# Confirm success by verifying that the billing form is filled
self.assertTrue(
self.wait.until(
self.page_loaded("body"),
message="The billing form was not filled"
))

except Exception as e:
# Log any exception that occurred during test execution.
logging.info(str(e))

def select_city_state(self, select):
# Helper method to select a city/state from the provided dropdowns
select.select_by_visible_text("Default store")

if __name__ == '__main__':
unittest.main()