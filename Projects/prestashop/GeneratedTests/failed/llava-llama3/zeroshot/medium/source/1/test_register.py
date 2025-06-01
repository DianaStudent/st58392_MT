from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegistrationProcess(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
self.email = f"test_{str(random.randint(1, 100)).@user.com"

def tearDown(self):
self.driver.quit()

def test_registration_process(self):
# Step 1: Open the home page
self.assertEqual(self.driver.title, "Home Page", "Failed to open Home Page")

# Step 2: Click on the login link in the top menu
self.assertTrue(self.driver.find_element_by_css_selector("a[data-name='login']"), "Login link not found")
self.driver.find_element_by_css_selector("a[data-name='login']").click()

# Step 3: Click on the register link on the login page
self.assertTrue(self.driver.find_element_by_css_selector("li>a[title='Register']"), "Register link not found")
self.driver.find_element_by_css_selector("li>a[title='Register']").click()

# Step 4: Fill in the registration form fields
gender = self.driver.find_element_by_css_selector("label[data-name='gender']")
first_name = self.driver.find_element_by_css_selector("input[data-name='first_name']")
last_name = self.driver.find_element_by_css_selector("input[data-name='last_name']")
email = self.driver.find_element_by_css_selector("input[data-name='email']")
password = self.driver.find_element_by_css_selector("input[data-name='password']")
birthday = self.driver.find_element_by_css_selector("input[data-name='birthday']")
checkboxes = self.driver.find_elements_by_css_selector("label[data-name='agree']")

# Step 5: Check required checkboxes
if len(checkboxes) < 2:
self.fail("Less than two checkbox options are available")
for checkbox in checkboxes:
if not checkbox.get_attribute("data-checked") == "yes":
checkbox.click()

# Step 6: Submit the form
self.assertTrue(self.driver.find_element_by_css_selector("button[data-name='submit']"), "Submit button not found")
self.driver.find_element_by_css_selector("button[data-name='submit']").click()

# Step 7: Confirm success by checking for the presence of  "Sign out" in the top bar
self.assertEqual(self.driver.title, "Profile Page", "Failed to open Profile Page")
self.assertTrue(self.driver.find_element_by_css_selector("a[data-name='signout']"), "Signout link not found")
self.driver.find_element_by_css_selector("a[data-name='signout']").click()

# Check required elements for existence and non-empty
self.assertTrue(gender, "Gender element not found")
self.assertTrue(first_name, "First name element not found")
self.assertTrue(last_name, "Last name element not found")
self.assertTrue(email, "Email element not found")
self.assertTrue(password, "Password element not found")
self.assertTrue(birthday, "Birthday element not found")

if self.email != email:
self.fail(f"Invalid email address: {email}")

if not len(checkboxes) == 2:
self.fail("Less than two checkbox options are available")

if self.driver.title != "Profile Page":
self.fail("Failed to open Profile Page")

if self.driver.find_element_by_css_selector("a[data-name='signout']") is None:
self.fail("Sign out link not found")
```sql
if __name__ == "__main__":
    unittest.main()
```
### Notes: