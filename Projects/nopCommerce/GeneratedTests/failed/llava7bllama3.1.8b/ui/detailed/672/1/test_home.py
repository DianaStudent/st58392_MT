from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://max/')

    def tearDown(self):
        self.driver.quit()

    def test_homepage_structural_elements(self):
        # Check header presence
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//header')))
        self.assertTrue(header.is_displayed())

        # Check navigation menu presence
        nav_menu = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//nav')))
        self.assertTrue(nav_menu.is_displayed())

        # Check footer presence
        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//footer')))
        self.assertTrue(footer.is_displayed())

    def test_input_fields_buttons_labels_sections(self):
        # Check input fields presence
        input_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'input')))
        for field in input_fields:
            self.assertTrue(field.is_displayed())

        # Check buttons presence
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'button')))
        for button in buttons:
            self.assertTrue(button.is_displayed())

        # Check labels presence
        labels = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'label')))
        for label in labels:
            self.assertTrue(label.is_displayed())

    def test_interact_with_ui_elements(self):
        # Click on a button
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        button.click()

        # Check UI reaction visually
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="ui-helper-hidden-accessible"]')))

if __name__ == '__main__':
    unittest.main()