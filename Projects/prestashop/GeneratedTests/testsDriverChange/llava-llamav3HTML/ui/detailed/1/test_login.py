import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Key
from selenium.webdriver.common.buttons import Button

class EcomTest(unittest.TestCase):
def setUp(self):
# Initialize the Chrome WebDriver
self.driver = webdriver.Chrome()

def tearDown(self):
# Close the browser window
self.driver.quit()

def test_Ecom(self):
try:
self.driver.get("http://localhost:8080/en/")
print("Loading...")
time.sleep(5)
assert self.assertTrue(self.wait_for_element_located((By.XPATH, "//header[@role='banner']")))

print("Header Found")
time.sleep(1)

# Check the presence and visibility of input fields, buttons, labels, and sections.
self.wait_for_element_located((By.XPATH, "//input[@id='password-1']"))
self.wait_for_element_located((By.XPATH, "//input[@id='email-1']"))
self.wait_for_element_register = self.wait_for_element_located((By.XPATH, "//button[@class='btn btn-primary btn-lg btn-rounded']"))

# Interact with key UI elements.
self.wait_for_element_clickable = self.wait_for_element_located((By.XPATH, "//a[@href='clothes']"))
self.wait_for_element_clickable.click()

print("Clothes Page Loaded")
time.sleep(5)

# Confirm that the UI reacts visually.
assert self.assertTrue(self.wait_for_element_located((By.XPATH, "//h1[contains(text(),'Welcome to PrestaShop')]")))
print("Welcome to PrestaShop")
time.sleep(3)

# Check the presence and visibility of input fields, buttons, labels, and sections.
self.wait_accessories = self.wait_for_element_located((By.XPATH, "//a[@href='accessories']"))
self.wait_accessories.click()

print("Accessories Page Loaded")
time.sleep(5)

assert self.assertTrue(self.wait_for_element_located((By.XPATH, "//h1[contains(text(),'Clothes')]")))
print("Clothes Page Loaded")
time.sleep(3)

# Confirm that the UI reacts visually.
assert self.assertTrue(self.wait_for_element_located((By.XPATH, "//h1[contains(text(),'Clothes')]")))
print("Clothes Page Loaded")
time.sleep(5)

# Check the presence and visibility of input fields, buttons, labels, and sections.
self.wait_register = self.wait_for_element_located((By.XPATH, "//button[@class='btn btn-primary btn-lg btn-rounded']"))
self.wait_register.click()

print("Register Page Loaded")
time.sleep(5)

# Confirm that the UI reacts visually.
assert self.assertTrue(self.wait_for_element_located((By.XPATH, "//h1[contains(text(),'PrestaShop')]")))
print("PrestaShop")
time.sleep(3)

# Check the presence and visibility of input fields, buttons, labels, and sections.
self.wait_login = self.wait_for_element_located((By.XPATH, "//button[@class='btn btn-primary btn-lg btn-rounded']"))
self.wait_login.click()

print("Login Page Loaded")
time.sleep(5)

assert self.assertTrue(self.wait_for_element_located((By.XPATH, "//h1[contains(text(),'PrestaShop')]")))
print("PrestaShop")
time.sleep(3)

# Confirm that the UI reacts visually.
assert self.assertTrue(self.wait_for_element_located((By.XPATH, "//h1[contains(text(),'PrestaShop)]"))
print("PrestaShop")
time.sleep(5)

# Check the presence and visibility of input fields, buttons, labels, and sections.
self.wait_register = self.wait_for_element_located((By.XPATH, "//button[@class='btn btn-primary btn-lg btn-rounded']"))
self.wait_register.click()

print("Register Page Loaded")
time.sleep(5)

assert self.assertTrue(self.wait_for_element_located((By.XPATH, "//h1[contains(text(),'PrestaShop)]")))
print("PrestaShop")
time.sleep(3)

# Confirm that the UI reacts visually.
assert self.assertTrue(self.wait_for_element_located((By.XPATH, "//h1[contains(text(''PrestaShop''')]"))
print("PrestaShop")
time.sleep(5)

except Exception as e:
self.fail(e)
if name == 'main':
unittest.main()