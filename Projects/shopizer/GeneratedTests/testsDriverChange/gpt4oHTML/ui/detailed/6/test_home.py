import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def test_ui_components(self):
        driver = self.driver

        # Wait for header to be visible
        try:
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'header.header-area'))
            )
        except Exception:
            self.fail("Header is missing or not visible")

        # Wait for footer to be visible
        try:
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer.footer-area'))
            )
        except Exception:
            self.fail("Footer is missing or not visible")

        # Check navigation menu
        try:
            nav_menu = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.main-menu nav'))
            )
            self.assertIn("Home", nav_menu.text)
            self.assertIn("Tables", nav_menu.text)
            self.assertIn("Chairs", nav_menu.text)
        except Exception:
            self.fail("Navigation menu is missing or not visible")

        # Check input field for subscribing in footer
        try:
            subscribe_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.email'))
            )
        except Exception:
            self.fail("Subscribe input field is missing or not visible")

        # Check visibility of buttons
        try:
            buttons = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button'))
            )
            self.assertTrue(len(buttons) > 0, "No buttons are present on the page")
        except Exception:
            self.fail("Buttons are missing or not visible")

        # Interacting with the 'Accept Cookies' button if present
        try:
            accept_cookies_btn = driver.find_element(By.ID, 'rcc-confirm-button')
            if accept_cookies_btn.is_displayed():
                accept_cookies_btn.click()
        except Exception:
            self.fail("'Accept Cookies' button is missing or not clickable")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()