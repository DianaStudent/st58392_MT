from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class TestRegisterScenario(unittest.TestCase):
def setUp(self):
self.url = "http://localhost:8080/en/"
self.credentials = {
gender: 1,
firstname: "Test",
lastname: "User",
email: f"test_{str(random.randint(10000, 100000)).}@user.com",
password: "test@user1"
}
def tearDown(self):
pass

def test_register(self):
# Step 1: Open the homepage
driver = webdriver.Chrome()
driver.get(self.url)

# Step 2: Click the login link from the top navigation
login_link = (By.XPATH, "//a[contains(text(), 'No account? Create one here')]")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable(login_link))
login_link.click()

# Step 3: Fill in the following fields using credentials:
gender_field = (By.XPATH, "//div[contains(data-name,'gender')]/label/input")
firstname_field = (By.XPATH, "//input[contains(data-name,'firstname')]")
lastname_field = (By.XPATH, "//input[contains(data-name,'lastname')]")
email_field = (By.XPATH, "//input[contains(data-name,'email')]")

gender_button = (By.XPATH, "//label[contains(text(),'Mr.')]")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable(gender_button))
gender_button.click()

firstname_field.send_keys(self.credentials["firstname"])
lastname_field.send_keys(self.credentials["lastname"])
email_field.send_keys(self.credentials["email"])

# Step 4: Tick checkboxes for privacy, newsletter, terms, etc.
privacy_checkbox = (By.XPATH, "//label[contains(text(),'Private')]/input")
newsletter_checkbox = (By.XPATH, "//label[contains(text('Newsletter')]")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable(privacy_checkbox))
privacy_checkbox.click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable(newspaper_