import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class CabinCaseRegistrationTest(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()
self.base_url = "http://localhost:8080/en/"
self.registration_page = self.base_url + "registration"

def tearDown(self):
self.driver.quit()

def test_registration_page_loads_with_required_elements_present(self):
try:
self.driver.get(self.registration_page)
assert self.is_element_present_by_css_selector(".first-name")
assert self.is_element_present_by_css_selector(".last-name")
assert self.is_element_present_by_css_selector(".mobile-number")
assert self.is_element_present_by_css_selector(".date-of-birth")
assert self.is_element_present_by_css_selector(".get-started")
assert self.is_element_present_by_css_selector(".register.now")
except Exception as e:
self.fail("Registration page failed to load with required elements present. " + str(e))

def is_element_present(self, css_selector):
try:
WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((css_selector)))
return True
except WebDriverException:
return False

if __name__ == '__main__':
unittest.main()