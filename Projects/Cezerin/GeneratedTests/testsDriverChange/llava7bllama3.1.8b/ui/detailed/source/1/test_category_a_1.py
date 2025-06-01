import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUITestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.driver.maximize_window()

    def test_ui_elements_present(self):
        # Structural Elements
        header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#header"))
        )
        footer = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#footer"))
        )

        # Main Content Area
        left_sidebar = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#left-sidebar"))
        )
        main_content_section = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#main-content-section"))
        )
        right_sidebar = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#right-sidebar"))
        )

        # Input Fields and Buttons
        search_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
        add_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )

        # Interact with key UI elements
        search_input.send_keys("test")
        add_button.click()

        # Assert that the UI reacts visually
        self.assertTrue(header.is_displayed())
        self.assertTrue(footer.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()