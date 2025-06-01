import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestRegister(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

def test_register(self):
# Open the homepage.
self.driver.get("http://max/")

# Click the "Register" link in the top navigation.
register_link = self.wait.until(EC.element_located((By.XPATH, "//a[contains(@class,'register-link')]")))
register_link.click()

# Wait for the registration form to load.
self.wait.until(EC.visibility_of_element_located((By.XPATH, "//form[contains(@id,\"registration-form\")]")))

# Select the appropriate gender radio input based on the provided data.
gender_input = self.wait.until(EC.element_located((By.XPATH, "//input[@name=\"Gender\" and @value=\"F\"]")))
gender_input.click()

# Fill in all required fields: first name, last name, email, company name, password, confirm password from credentials.
first_name_field = self.wait.until(EC.element_located((By.XPATH, "//input[contains(@id,\"FirstName\")]"))
last_name_field = self.wait.until(EC.element_located((By.XPATH, "//input[contains(@id,\"LastName\")]"))
email_field = self.wait.until(EC.element_located((By.XPATH, "//input[contains(@id,\"Email\")]"))
company_name_field = self.wait.until(EC.element_located((By.XPATH, "//input[contains(@id,\"Company\")]"))
password_field = self.wait.until(EC.element_located((By.XPATH, "//input[contains(@id,\"Password\")]")))
confirm_password_field = self.wait.until(EC.element_located((By.XPATH, "//input[contains(@id,\"ConfirmPassword\")]")))

first_name_field.send_keys("Test")
last\_name\_field.send\_keys("User")
email\_field.send\_keys("test@gmail.com")
company\_name\_field.send\_keys("TestCorp")
password\_field.send\_keys("test11")
confirm\_password\_field.send\_keys("test11")

# Submit the registration form.
register_button = self.wait.until(EC.element_located((By.XPATH, "//button[contains(@class,\"register-continue-button\")]")))
register\_button.click()

# Wait for the response page or confirmation message to load.
self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,\"result\") and @role=\"alert\"]")))

# Verify that registration succeeded by checking:
if self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),\"Your registration completed\")]")))):
self.assertTrue(True)
else:
self.fail("Registration failed")

if \_\_name\_\_ == "\_\_main\_\_":
unittest.main()