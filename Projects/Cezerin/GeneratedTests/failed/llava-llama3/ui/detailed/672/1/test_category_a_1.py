from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from utilities.selenium import wait_for_element_to_appear

class TestPythonSelenium(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

def test_load_page(self):
self.wait.until(By.XPATH, "//html/body")
assert self.driver.current_url == "http://localhost:3000"

def test_category_a_1(self):
self.wait.until_not(By.XPATH, "//a[@href=\"category-1\"]")

def test_profile_fields(self):
self.wait.until_not(By.XPATH, "//label[contains(text(), 'your logo')]")
self.wait.until_not(By.XPATH, "//input[contains(@type, 'text') and @name='username']")
self.wait.until_not(By.XPATH, "//button[contains(@class,'btn btn-primary')]")

if __name__ == '__main__':
unittest.main()