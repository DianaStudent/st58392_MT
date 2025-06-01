import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import WebDriverWait
import os

class TestRegisterPage(unittest.TestCase):
    def setUp(self):
        # setup for the test case
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # teardown for the test case
        self.driver.quit()

    def test_register_page(self):
        # Check that the main UI components are present:
        self.assertTrue(self.driver.find_element_by_css_selector("header"))
        self.assertTrue(self.driver.find_element_by_css_selector("div.container"))

        # Check that these elements exist and are visible:
        self.assertTrue(self.driver.find_element_by_id("first-name"))
        self.assertTrue(self.driver.find_element_by_id("last-name"))
        self.assertTrue(self.driver.find_element_by_id("email"))

        # Check for the registration button
        self.assertTrue(self.driver.find_element_by_css_selector("button[type='submit']"))
        self.assertTrue(self.driver.find_element_by_link_text("Register now"))

        # Check if there's an existing account option
        self.assertTrue(self.driver.find_element_by_link_text("Already have an account? Sign in"))

def main():
if __name__ == "__main__":
unittest.main()

if os.environ["TESTING"]:
else:
main()
```