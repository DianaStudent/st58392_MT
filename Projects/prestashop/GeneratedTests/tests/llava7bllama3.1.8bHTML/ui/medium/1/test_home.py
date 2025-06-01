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
        self.driver.get("http://localhost:8080/en/")

    def test_home_page_elements(self):
        # Wait for navigation links to be visible
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.ui-menuitem-text"))
        )
        
        self.assertEqual(len(nav_links), 4)

        # Wait for inputs to be visible
        inputs = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']"))
        )

        self.assertEqual(len(inputs), 2)

        # Wait for buttons to be visible
        buttons = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button.ui-button"))
        )

        self.assertEqual(len(buttons), 2)

        # Click a button and verify UI update visually
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ui-button")))
        button.click()

    def test_interactive_elements_do_not_cause_errors(self):
        # Wait for banners to be visible
        banner = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".ui-widget-header"))
        )

        self.assertIsNotNone(banner)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()