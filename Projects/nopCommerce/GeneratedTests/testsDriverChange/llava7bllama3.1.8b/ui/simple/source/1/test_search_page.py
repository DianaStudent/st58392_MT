import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class MaxTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def test_search_page_elements(self):
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-helper-hidden-accessible"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='q']"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
        )

        # Check that these elements exist and are visible
        search_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='q']")
        self.assertIsNotNone(search_input)
        self.assertTrue(search_input.is_displayed())

        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        self.assertIsNotNone(submit_button)
        self.assertTrue(submit_button.is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()