from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestGympersetLogin(unittest.TestCase):
def setUp(self):
driver = webdriver.Chrome(ChromeDriverManager().get_driver_path())
self.driver = driver

def tearDown(self):
self.driver.quit()

def test_login_page(self):
try:
self.assertEqual(self.driver.title, "Gymperset")
header = WebDriverWait(self.driver, 20).until(
EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Gymperset')]")))
)

sign_up_button = WebDriverWait(self.driver, 20).until(
EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Sign Up')]"))
)

self.driver.execute_script("arguments[0].click();", sign_up_button)
login_button = WebDriverWait(self.driver, 20).until(
EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Log In')]"))
)

username_input = self.driver.find_element_by_id("username")
password_input = self.driver.find_element_by_id("password")

username_input.send_keys("test_username")
password_input.send_keys("test_password")

login_button.click()

welcome_text = WebDriverWait(self.driver, 20).until(
EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Welcome to Gymperset')]"))
)

except Exception as e:
self.fail(str(e))

if __name__ == '__main__':
unittest.main()