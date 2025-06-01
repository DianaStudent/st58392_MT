from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import alert, confirm
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.utils import _element_to_logger

# HTML data to use for the test case
html_data = {
"home\_before\_register": "<body> <input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"CfDJ8F0-u7sVjGpKmfv7esau8ub21TLdlVsv4EsIuP2UXLINkzdVWTzyn\_nDxLaSl9py2\_Ipfzr\_a2UafzMGapAqGaWTUzlafXswY\_9HGO3MF2ka0rlqwj7itnqMV8a0l1zGX7WV2j8g3W4odcp8nqHOI0E\"/> </body>",
"register\_page": "<body> <input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"CfDJ8F0-u7sVjGpKmfv7esau8uatX1FRYjCMYdh0oXCXQkOxOfvUX5g0B6B9E4H73T14UkvxecobYasVdX4VrK4- ngYJPtVZqwJQQpllr6e6MWKXo\_boPgi1rY8IN8GmMx0oyx- tEFWBdI7OYSGKXwEDO8\"/> <div class=\"master-wrapper-page\"> <div class=\"master-wrapper-content\" id=\"main\" role=\"main\"> <div class=\"master-column-wrapper\"> <div class=\"center-1\"> <div class=\"page registration-page\"> <div class=\"page-title\"> <h1>Register</h1> </div> <div class=\"page-body\"> <div class=\"form-fields\"> <div class=\"inputs\"> <label for=\"gender\">Gender:</label> <div class=\"gender\" id=\"gender\"> <span class=\"male\"> <input id=\"gender- male\" name=\"Gender\" type=\"radio\" value=\"M\"/> <label class=\"forcheckbox\" for=\"gender- male\">Male</label> </span> <span class=\"female\"> <input checked=\"checked\" data-val=\"true\" data-val-required=\"The Newsletter field is required.\" id=\"Newsletter\" name=\"Newsletter\" type=\"checkbox\" value=\"true\"/> </div> <div class=\"inputs\"> <label for=\"Password\">Password:</label> <input data-val=\"true\" data-val-regex=\"Password must meet the following rules: must have at least 6 characters and not greater than 64 characters\" data-val-regex-pattern=\"^.{6,64}$\" id=\"Password\" name=\"Password\" type=\"password\"/> <span class=\"required\">*</span> </div> <div class=\"inputs\"> <label for=\"ConfirmPassword\">Confirm password:</label> <input data-val=\"true\" data-val-equalto=\"The password and confirmation password do not match.\" data-val- equalto-other=\"*.Password\" id=\"ConfirmPassword\" name=\"ConfirmPassword\" type=\"password\"/> <span class=\"required\">*</span> </div> </div> <div class=\"buttons\"> <a class=\"button-1 register-continue-button\" href=\"/\">Continue</a> </div> </div> </div> </div> </body>",
"register\_result": "<body> <input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"CfDJ8F0-u7sVjGpKmfv7esau8uZbBm4vE2jCORlw3roFmaVpZtlNVu8bAh4GPJw7hnU0IH92xQnrBlT- b-2fETxfBxuHJaNCSTmvYx8w-z01ET8CbkUvWuWPYA\"/> <div class=\"master-wrapper-page\"> <div class=\"master-wrapper-content\" id=\"main\" role=\"main\"> <div class=\"master-column-wrapper\"> <div class=\"center-1\"> <div class=\"page registration-result-page\"> <div class=\"page-title\"> <h1>Register</h1> </div> <div class=\"page-body\"> <div class=\"result\"> Your registration completed </div> <div class=\"buttons\"> <a class=\"button-1 register-continue-button\" href=\"/\">Continue</a> </div> </div> </div> </div> </body>",
}

class TestRegisterPage(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test\_register(self):
# Open the homepage
self.driver.get("http://max/")

# Click the "Register" link in the top navigation
reg\_link = self.waitForElement(locator="html_ data/home\_before\_register")
self.driver.find\_element(by=reg\_link).click()

# Wait for the registration form to load
self.waitForPageLoad()

# Select the appropriate gender radio input based on the provided data
gender\_radio = self.waitForElement(locator="html_ data/register\_page")
selectGender = Select(self.waitForElement(locator="html_ data/register\_page"))
selectGender.selectByValue("M")

# Fill in all required fields: first name, last name, email, company name, password, confirm password from credentials
firstName = self.waitForElement(locator="html_ data/register\_page")
lastName = self.waitForElement(locator="html_ data/register\_page")
email = self.waitForElement(locator="html_ data/register\_page")
companyName = self.waitForElement(locator="html_ data/register\_page")
password = self.waitForElement(locator="html_ data/register\_page")
confirmPassword = self.waitForElement(locator="html_ data/register\_page")

# Submit the registration form
registerButton = self.waitForElement(locator="html_ data/register\_page")
self.driver.find\_element(by=registerButton).click()

# Wait for the response page or confirmation message to load
registerResult = self.waitForElement(locator="html_ data/register\_result")
if "Your registration completed" in self.waitForElement(locator="html_ data/register\_result").text:
assert (True)
else:
self.fail("Registration failed")

def waitForPageLoad(self):
# Use WebDriverWait to check if the element is present and visible within 20 seconds
def waitForElement(self, locator):
return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, locator)))

if \_\_name\_\_ == "\_\_main\_\_":
unittest.main()