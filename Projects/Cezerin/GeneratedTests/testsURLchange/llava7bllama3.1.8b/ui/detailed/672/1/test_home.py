import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    def test_ui_elements(self):
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#header')))
        self.assertTrue(header.is_displayed())

        # Footer
        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#footer')))
        self.assertTrue(footer.is_displayed())

        # Navigation
        navigation = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#navigation')))
        self.assertTrue(navigation.is_displayed())

        # Input fields
        input_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input')))
        for field in input_fields:
            self.assertTrue(field.is_displayed())

        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))
        for button in buttons:
            self.assertTrue(button.is_displayed())

        # Labels and sections
        labels_and_sections = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.label, .section')))
        for element in labels_and_sections:
            self.assertTrue(element.is_displayed())

    def test_interaction(self):
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()