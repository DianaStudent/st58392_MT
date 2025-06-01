from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_ui_elements(self):
        # Navigation links
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "nav > a"))
        )
        
        # Inputs and buttons
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#search-bar-input"))
        )

        # Clicking on the primary button should not cause errors
        self.driver.find_element_by_css_selector("button.primary-button").click()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()