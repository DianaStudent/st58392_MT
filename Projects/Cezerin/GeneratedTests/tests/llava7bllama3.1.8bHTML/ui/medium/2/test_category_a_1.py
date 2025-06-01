import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import html_data  # Assuming this is your HTML string

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(html_data)

    def tearDown(self):
        self.driver.quit()

    def test_home_page_elements(self):
        # Navigation links
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav a"))
        )
        self.assertGreater(len(navigation_links), 0)

        # Inputs
        inputs = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']"))
        )
        self.assertGreater(len(inputs), 0)

        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button"))
        )
        self.assertGreater(len(buttons), 0)

        # Banners
        banners = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#banner"))
        )
        self.assertIsNotNone(banners)

    def test_interactive_elements(self):
        # Click a button and verify UI updates visually
        button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        button.click()

        # Verify interactive elements do not cause errors in the UI
        self.driver.save_screenshot("test_interactive_elements.png")

if __name__ == "__main__":
    unittest.main()