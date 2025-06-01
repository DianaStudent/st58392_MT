import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000")

    def test_ui_elements(self):
        # Header presence
        header_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "header"))
        )
        self.assertIsNotNone(header_element)

        # Footer presence
        footer_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "footer"))
        )
        self.assertIsNotNone(footer_element)

        # Navigation menu presence
        nav_menu_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-menu"))
        )
        self.assertIsNotNone(nav_menu_element)

        # Form fields presence
        form_fields_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form"))
        )
        self.assertIsNotNone(form_fields_element)

        # Button presence
        button_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-button"))
        )
        self.assertIsNotNone(button_element)

    def test_button_clickability(self):
        # Click on the button
        button_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button"))
        )
        button_element.click()

        # Wait for the button to change its state (e.g., become inactive)
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".checkout-button"))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()