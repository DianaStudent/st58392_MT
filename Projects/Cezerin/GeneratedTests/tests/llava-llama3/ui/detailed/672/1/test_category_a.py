import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Key
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager import ChromeDriverManager

class TestSelenium(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())

def tearDown(self):
self.driver.quit()

def test_load_page(self):
self.assertEqual(EC.visibility_of_element_located((By.XPATH, "//body[role='application']")),"Header is visible")

def test_category_a(self):
self.assertEqual(EC.visibility_of_element_located((By.XPATH, "//body[role='application']")),"Category A is visible")

def test_category_a_1(self):
self.assertEqual(EC.visibility_of_element_located((By.XPATH, "//body[role='application']")),"Category 1 is visible")

if __name__ == '__main__':
unittest.main()
```