from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestWebsite(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        # Structural elements
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'header')))
        self.assertTrue(header.is_displayed())

        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'footer')))
        self.assertTrue(footer.is_displayed())

        nav = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nav li a')))
        self.assertTrue(nav.is_displayed())

        # Input fields
        input_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]')))
        self.assertTrue(input_email.is_displayed())

        input_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
        self.assertTrue(input_password.is_displayed())

        # Buttons
        button_submit = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        self.assertTrue(button_submit.is_displayed())

        # Labels and sections
        label_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="email"]')))
        self.assertTrue(label_email.is_displayed())

        section_register = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#register-section')))
        self.assertTrue(section_register.is_displayed())

        # Interact with key UI elements
        button_submit.click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.toast')))

        # Assert that no required UI element is missing
        self.assertTrue(header.is_displayed())
        self.assertTrue(footer.is_displayed())
        self.assertTrue(nav.is_displayed())
        self.assertTrue(input_email.is_displayed())
        self.assertTrue(input_password.is_displayed())
        self.assertTrue(button_submit.is_displayed())
        self.assertTrue(label_email.is_displayed())
        self.assertTrue(section_register.is_displayed())

if __name__ == '__main__':
    unittest.main()