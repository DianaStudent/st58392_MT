from selenium import webdriver
from selenium.webdriver.common.keys import Key
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestSelenium(unittest.TestCase):

def setUp(self):
# Set up the ChromeDriver using WebDriver-Manager.
self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def tearDown(self):
# Close the browser window after each test run.
self.driver.quit()

def test\_interface_elements\_presence(self):
# Check that all required elements are present in the main page.

url = "http://localhost:8080/en/"
self.driver.get(url)

headers = self.driver.find\_element\_by\_css("h1")
inputs = self.driver.find\_elements\_by\_css("input")
buttons = self.driver.find\_elements\_by\_css("button")

assert headers is not None
assert len(inputs) > 0
assert len(buttons) > 0

def test\_click\_button(self):
# Click a button and confirm the UI updates visually.

url = "http://localhost:8080/en/3-"
self.driver.get(url)

button = self.wait.until(EC.element\_to\_be\_clickable("css selector", "a[title='Clothes']"))
button.click()

assert "Clothes" in self.driver.title

def test\_register(self):
# Test the registration page.

url = "http://localhost:8080/en/registration"
self.driver.get(url)

email = self.wait.until(EC.element\_to\_be\_clickable("css selector", "#email\_register"))
password = self.wait.until(EC.element\_to\_be\_clickable("css selector", "#password\_register"))

email.send\_keys("\u00e6@gmail.com")
password.send\_keys("\u00e6\u00a1\u00e6\u00e6\u00e6\u00e5")

submit = self.wait.until(EC.element\_to\_be\_clickable("css selector", "#registerBtn"))
submit.click()

assert "Thank you. You have been logged in." in self.driver.title

if \_\_name\_\_ == "\_\_main\_\_\_":
unittest.main()