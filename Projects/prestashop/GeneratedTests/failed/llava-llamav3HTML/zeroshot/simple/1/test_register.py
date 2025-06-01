from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.actions import ActionChains
from selenium.webdriver.common.alert import Alert

class TestRegistration(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_registration(self):
try:
# Email field
email_field = WebDriverWait(self.driver, 20).until(
By.XPATH,
'//input[@type="email" and @data-name="email"]'
)

# Password field
password_field = self.driver.find_element_by_name('password')

# Confirm checkbox
confirm_checkbox = self.driver.find_element_by_id('confirm')
assert confirm_checkbox.is_selected()

# Proceed button
proceed_button = WebDriverWait(self.driver, 20).until(
By.XPATH,
'//button[@type="button" and @data-name="proceed"]'
)

# Sign out link
sign_out_link = WebDriverWait(self.driver, 20).until(
By.XPATH,
'//a[@data-name="sign-out"]'
)
except:
self.fail("Required element missing")

if __name__ == '__main__':
unittest.main()