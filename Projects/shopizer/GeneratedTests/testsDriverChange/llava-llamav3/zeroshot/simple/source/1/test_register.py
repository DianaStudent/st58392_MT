import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
class TestRegistration(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
self.wait = WebDriverWait(self.driver, 20)
def tearDown(self):
self.driver.quit()
def test_registration(self):
try:
# Fill the name field
name_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='userName']")))
name_input.send_keys("Test User")
# Fill the email field with a dynamically generated email
email_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='userEmail']")))
email_input.send_keys(self.generate_email())
# Fill the password and repeat password fields with the same value
password_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='userPassword']")))
repeat_password_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='repeatPassword']")))
password_input.send_keys("test**11")
repeat_password_input.send_keys("test**11")
# Click the "Register" button
register_button = self.wait.until(EC.element_to_click((By.XPATH, "//button[@value='Register']")))
register_button.click()
# Confirm success by checking that the browser is redirected to a page containing "/my-account"
success_url = self.wait.until(EC.url_contains("/my-account"))
self.assertEqual(success_url, "http://localhost:8080/my-account/")
except Exception as e:
self.fail(str(e))
def generate_email(self):
return "test_user" + str(time.time())
if __name__ == '__main__':
unittest.main()