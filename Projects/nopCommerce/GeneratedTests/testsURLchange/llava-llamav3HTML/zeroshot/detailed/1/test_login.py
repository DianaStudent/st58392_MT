import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class LoginTest(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_login(self):
# 1. Open the home page.
self.driver.get("http://max/")
print("Step 1 passed")

# 2. Click the "Login" button in the top navigation.
login_button_xpath = "//input[@name='__RequestVerificationToken']"
login_button_text = "Login"
self.assertTrue(self.is_element_present(login_button_xpath))
self.assertTrue(self.is_element_present(login_button_text))

# 3. Wait until the login page loads fully
WebDriverWait(self.driver, 20).until(lambda x: self.is_element_present("//input[@name='__RequestVerificationToken']"))

# 4. Fill in the email and password fields using the provided credentials.
email_xpath = "//input[@name='Email']"
password_xpath = "//input[@name='Password']"
self.assertTrue(self.is_element_present(email_xpath))
self.assertTrue(self.is_element_present(password_xpath))

email_field = self.wait_for_element(email_xpath, 20)
password_field = self.wait_for_element(password_xpath, 20)

email_field.send_keys("admin@admin.com")
password_field.send_keys("admin")

# 5. Click the login button.
login_button = self.wait_for_element(login_button_xpath, 20)
login_button.click()

print("Step 5 passed")

# 6. Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
logout_button_xpath = "//span[contains(text(), ' Logout')]"
logout_button_text = "Logout"
self.assertTrue(self.is_element_present(logout_button_xpath))
self.assertTrue(self.is_element_present(logout_button_text))

def is_element_present(self, xpath):
try:
element = self.driver.find_element_by_xpath(xpath)
return element
except NoSuchElementException:
return False

if __name__ == '__main__':
unittest.main()