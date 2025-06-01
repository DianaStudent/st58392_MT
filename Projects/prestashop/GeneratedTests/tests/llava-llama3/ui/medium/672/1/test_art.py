import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.checkbox import Checkbox
from selenium.webdriver.support.alert import Alert
from selenium.webdriver.support.button import Button

class TestArtSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_art_selenium(self):
        # Open the page
        self.driver.get("http://localhost:8080/en/9-art")

        # Confirm the presence of key interface elements
        navigation_links = self.driver.find_elements_by_tag_name('a')
        inputs = self.driver.find_elements_by_tag_name('input')
        buttons = self.driver.find_elements_by_tag_name('button')
        form_fields = self.driver.find_elements_by_tag_name('form')

        for link, input in zip(navigation_links, inputs):
            self.assertTrue(link.is_displayed())
            self.assertTrue(input.is_displayed())

        for button in buttons:
            self.assertTrue(button.is_displayed())

        # Interact with one or two elements
        art_button = WebDriverWait(self.driver, 20).until(ec=EC.element_to_be_clickable((By.XPATH, "//button[@id='art-button']")))
        art_button.click()

        # Verify that interactive elements do not cause errors in the UI
        # Check if alert appears and has expected text
        alert = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Please log in to continue your session')]")))
        )
        self.assertTrue(alert.is_displayed())
        self.assertEqual("Please log in to continue your session", alert.text)

if __name__ == '__main__':
    unittest.main()