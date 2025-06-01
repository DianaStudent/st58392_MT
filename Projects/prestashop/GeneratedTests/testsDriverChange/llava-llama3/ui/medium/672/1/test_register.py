import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPage(unittest.TestCase):
def setUp(self):
driver = webdriver.Chrome(ChromeDriverManager().get_chromedriver())
self.driver = driver
super().setUp()

def tearDown(self):
self.driver.quit()

def test_registration_page(self):
# 1. Open the page.
self.driver.get("http://localhost:8080/en/")

# Check that key interface elements are present and visible.
self.assertTrue("Sign up" in self.driver.title)
self.assertTrue(self.driver.find_element_by_name("first\_name"))
self.assertTrue(self.driver.find_element_by_name("last\_name"))
self.assertTrue(self.driver.find_element_by_name("email"))

# 2. Interact with an element — e.g., click a button and check that the UI updates visually.
button = self.driver.find_element_by_css_selector(".btn btn-primary")
button.click()
WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Signed up successful')]")

# Verify that interactive elements do not cause errors in the UI.
try:
self.driver.get("http://localhost:8080/en/")
except WebDriverException as e:
self.fail("Registration failed with error message " + str(e))

# If any required element is missing, fail the test using self.fail(...).
else:
self.assertTrue(button.get\_attribute("data-original-title"))
self.assertTrue(self.driver.find_element_by_name("first\_name").get\_attribute("placeholder"))
self.assertTrue(self.driver.find_element_by_name("last\_name").get\_attribute("placeholder"))
self.assertTrue(self.driver.find_element_by_name("email").get\_attribute("placeholder"))

if __name__ == "\_\_main\_\_":
unittest.main()