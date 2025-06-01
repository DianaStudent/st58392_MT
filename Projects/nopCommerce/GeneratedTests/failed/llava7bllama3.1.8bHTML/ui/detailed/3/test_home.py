from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        # Wait for 20 seconds to ensure all elements are loaded
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        
        # Check presence and visibility of header
        header = self.driver.find_element(By.TAG_NAME, "header")
        self.assertTrue(header.is_displayed())

        # Check presence and visibility of input fields
        input_fields = self.driver.find_elements(By.TAG_NAME, "input")
        for field in input_fields:
            self.assertTrue(field.is_displayed())

        # Check presence and visibility of buttons
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            self.assertTrue(button.is_displayed())

        # Check presence and visibility of labels
        labels = self.driver.find_elements(By.TAG_NAME, "label")
        for label in labels:
            self.assertTrue(label.is_displayed())

        # Check presence and visibility of sections
        sections = self.driver.find_elements(By.TAG_NAME, "section")
        for section in sections:
            self.assertTrue(section.is_displayed())

        # Interact with key UI elements (e.g., click buttons)
        self.driver.find_element(By.TAG_NAME, "button").click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "new-element")))

        # Assert that no required UI element is missing
        self.failUnless(header)
        for field in input_fields:
            self.failUnless(field)
        for button in buttons:
            self.failUnless(button)
        for label in labels:
            self.failUnless(label)
        for section in sections:
            self.failUnless(section)

if __name__ == '__main__':
    unittest.main()