import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegisterProcess(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_register_process(self):
# 1. Open the home page.
self.driver.get('http://localhost/')

# 2. Click on the account button and select "Register".
account_button = self.wait_for_element_by_css_selector('a[role="button"][href="/my-account"]')
register_button = WebDriverWait(account_button, 20).until(EC.element_to_be_clickable('a'))
register_button.click()

# 3. Fill in the registration form.
first_name_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable('input[name="firstName"]'))
last_name_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable('input[name="lastName"]'))
email_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable('input[name="email"]'))
password_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable('input[name="password"]'))

# Fill all fields for registration.
self.first_name_field.send_keys('Test')
self.last_name_field.send_keys('User')

# 4. Select a country and a region/state.
country_element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable('label[for="selectCountry"]'))
region_element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable('label[for="selectRegion"]'))

# Submit the registration form.
self.submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable('button[type="submit"]'))
self.submit_button.click()

# Wait for redirect and confirm success by checking if the current URL
# includes "/my-account" in the URL.
success_url = self.wait_for_element_by_css_selector('a[role="button"][href="/my-account"]')
if not self.driver.current_url().includes("/my-account"):
self.fail("Registration failed. Please check your fields and try again.")

def wait_for_element_by_css_selector(self, css_selector):
try:
return WebDriverWait(self.driver, 20).until(EC.element_located((By.CSS_SELECTOR, css_selector)))
except NoSuchElementException:
return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

if __name__ == '__main__':
unittest.main()