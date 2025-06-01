import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class TestLogin(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_login(self):
try:
# Home page
self.driver.get('http://max/')

# Login link click
login_link = self.driver.find_element_by_css_selector('a[title="Log in"]')
login_link.click()
WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[contains("Email")]')))

# Email input
email_input = self.driver.find_element_by_name('email')

# Password input
password_input = self.driver.find_element_by_name('password')

# Fill in email and password inputs
email_input.send_keys('admin@admin.com')
password_input.send_keys('admin')

# Click login button
login_button = self.driver.find_element_by_css_selector('button.login-button')
login_button.click()

# Verify logged in by checking "Log out" button
logout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[contains("Log out")]')))
self.assertTrue(logout_button)

except Exception as e:
self.fail(str(e))

if \_\_name\_\_ == '\_\_\_\_':
unittest.main()