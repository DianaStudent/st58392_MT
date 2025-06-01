import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_key_interface_elements_present(self):
        # Navigation links
        navigation_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href^="/"]')))
        self.assertGreater(len(navigation_links), 0)

        # Inputs and buttons
        inputs_and_buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input, button')))
        self.assertGreater(len(inputs_and_buttons), 0)

        # Banners (if present)
        banners = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.banner')))
        if banners:
            self.assertEqual(banners.text, "Hello World!")
        else:
            self.fail("Banners not found")

    def test_login_button_clickable_and_updates_ui(self):
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        login_button.click()

        # Wait for UI to update
        updated_elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.updated-element')))
        self.assertGreater(len(updated_elements), 0)

    def test_no_errors_on_interaction(self):
        # Interact with an element (e.g., click a button)
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        login_button.click()

        # Wait for UI to update
        updated_elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.updated-element')))

        # Check that no JavaScript errors occurred
        js_errors = self.driver.find_element(By.TAG_NAME, 'body').text
        if "Error" in js_errors:
            self.fail("JavaScript error detected")

if __name__ == "__main__":
    unittest.main()