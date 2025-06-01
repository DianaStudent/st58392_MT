from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestInterface(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_interface_elements(self):
        # Navigation links
        navigation_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav a")))
        for link in navigation_links:
            self.assertEqual(link.is_enabled(), True)

        # Inputs
        inputs = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input")))
        for input_field in inputs:
            self.assertEqual(input_field.is_displayed(), True)

        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button")))
        for button in buttons:
            self.assertEqual(button.is_enabled(), True)

        # Banners
        banners = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".banner")))
        for banner in banners:
            self.assertEqual(banner.is_displayed(), True)

    def test_interact_with_button(self):
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        button.click()
        # Check that the UI updates visually
        updated_elements = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".updated-elements")))
        self.assertEqual(len(updated_elements), 1)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()