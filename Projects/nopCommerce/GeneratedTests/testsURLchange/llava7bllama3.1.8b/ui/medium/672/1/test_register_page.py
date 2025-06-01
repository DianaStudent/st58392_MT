import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")

    def tearDown(self):
        self.driver.quit()

    def test_registration_page_elements(self):
        # Confirm the presence of key interface elements
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-links a"))
        )
        form_inputs = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "form input"))
        )
        buttons = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button"))
        )

        # Check that interactive elements do not cause errors in the UI
        self.assertEqual(len(navigation_links), len(form_inputs))
        self.assertEqual(len(form_inputs), len(buttons))

    def test_registration_page_interaction(self):
        # Interact with one or two elements — e.g., click a button and check that the UI updates visually.
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()

        # Verify that interactive elements do not cause errors in the UI
        self.assertTrue(EC.visibility_of_element_located((By.CSS_SELECTOR, ".success-message")).__bool__)

if __name__ == "__main__":
    unittest.main()