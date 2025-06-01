from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class LoginTest(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()
self.url = "http://max/"
self.email = "admin@admin.com"
self.password = "admin"

def tearDown(self):
self.driver.quit()

def test_login(self):
# Open the home page
self.driver.get(self.url)
# Click the "Login" button in the top navigation
login_button = WebDriverWait(self.driver, 20).until(element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
ActionChains(self.driver).move_to_element(login_button).click()
# Fill in the email and password fields using the provided credentials
email_field = WebDriverWait(self.driver, 20).until(element_to_be_clickable((By.XPATH, "//input[contains(@data-val, 'true')]/../label[contains(text(), 'Email:')]")))
ActionChains(self.driver).move_to_element(email_field)
ActionChains(self.driver).send_keys(self.email)
password_field = WebDriverWait(self.driver, 20).until(element_to_be_clickable((By.XPATH, "//input[contains(@data-val, 'true')]/../label[contains(text(), 'Password:')]")))
ActionChains(self.driver).move_to_element(password_field)
ActionChains(self.driver).send_keys(self.password)
# Click the login button
login_button = WebDriverWait(self.driver, 20).until(element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log in')]")))
ActionChains(self.driver).move_to_element(login_button).click()
# Verify that the user is logged in by checking the "Log out" button is present in the top navigation
logout_button = WebDriverWait(self.driver, 20).until(element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Administration')]")))
ActionChains(self.driver).move_to_element(logout_button)
if not self.driver.current_url == self.url + "Admin":
self.fail("Failed to login")

if name == "__main__":
unittest.main()