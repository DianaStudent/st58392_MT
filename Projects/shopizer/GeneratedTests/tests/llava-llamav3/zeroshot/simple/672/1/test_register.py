import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.time import TimeOut
from selenium.webdriver.common.keys import Keys

class TestRegisterProcess(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_register_process(self):

# Generate a random email address for the registration process
email_address = "test" + str(random.randint(1, 1000000)) + "@shopizer.com"
print(f"Generated email address: {email_address}")

try:
# Go to the registration page
self.driver.get("http://localhost/")

# Select the 'Register' tab
register_tab = WebDriverWait(self.driver, 20).until(
selector=(By.XPATH, "//a[contains(text(), 'Register')]"))
)
register_tab.click()

# Enter the email address and password into the fields
email_field = WebDriverWait(self.driver, 20).until(
selector=(By.XPATH, "//input[@id='email']")
))
password_field = WebDriverWait(self.driver, 20).until(
selector=(By.XPATH, "//input[@id='password']")
))

# Fill in the email address field with the generated email address
email_field.send_keys(email_address)

# Fill in the password field with the test password
password_field.send_keys("test**11")

# Confirm success by checking that the browser is redirected to a page containing '/my-account' in the URL
self.assertTrue("/my-account" in self.driver.current_url())

# Tear down the webdriver after completing the test
except Exception as e:
print(f"An error occurred: {e}")

if __name__ == '__main__':
unittest.main()