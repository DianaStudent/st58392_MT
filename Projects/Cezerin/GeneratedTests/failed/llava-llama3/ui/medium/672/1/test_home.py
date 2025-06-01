from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=Options(headless=True))

    def tearDown(self):
        self.driver.quit()

    def test_selenium(self):
        # Open the page.
        self.driver.get("http://localhost:3000")

        # Confirm the presence of key interface elements
        time.sleep(2)
        self.assertTrue(self.element_exists_by_selector('header'))
        self.assertTrue(self.element_exists_by_selector('button'))
        self.assertTrue(self.element_exists_by_selector('input'))
        self.assertTrue(self.element_exists_by_selector('form'))
        self.assertTrue(self.element_exists_by_selector('link'))
        self.assertTrue(self.element_exists_by_selector('banner'))

        # Interact with one element - click a button and check that the UI updates visually.
        time.sleep(2)
        self.driver.find_element_by_css_selector('button').click()
        time.sleep(2)
        self.assertTrue(self.ui_updates())

        # Verify that interactive elements do not cause errors in the UI.
        time.sleep(2)
        self.assertTrue(not(self.element_causes_error()))

    def element_exists_by_selector(self, selector):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((selector, ''))
            )
            return True
        except WebDriverTimeoutException:
            return False

    def ui_updates(self):
        time.sleep(2)
        self.assertTrue(not(self.element_text_changed()))

    def element_causes_error(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((selector, ''))
            )
            return False
        except WebDriverTimeoutException:
            return True

    def element_text_changed(self):
        time.sleep(2)
        self.assertTrue(not(self.element_text_changed()))

if __name__ == '__main__':
    unittest.main()