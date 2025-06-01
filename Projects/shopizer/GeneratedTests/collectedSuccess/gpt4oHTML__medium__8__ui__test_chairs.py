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
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_components(self):
        driver = self.driver

        # Wait for and check presence of header elements
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".header-area"))
            )
        except:
            self.fail("Header area not found in the UI")

        # Check for navigation links
        navigation_links = [
            (By.LINK_TEXT, "Home"),
            (By.LINK_TEXT, "Tables"),
            (By.LINK_TEXT, "Chairs"),
            (By.LINK_TEXT, "Login"),
            (By.LINK_TEXT, "Register"),
        ]

        for selector in navigation_links:
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(selector)
                )
                self.assertTrue(element.is_displayed(), f"{selector[1]} link is not visible")
            except:
                self.fail(f"{selector[1]} link not found in the UI")

        # Check for input fields (e.g., subscribe email)
        try:
            input_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
            )
            self.assertTrue(input_field.is_displayed(), "Subscribe email input field is not visible")
        except:
            self.fail("Subscribe email input field not found in the UI")

        # Check for buttons
        try:
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
            )
            self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")
        except:
            self.fail("Accept cookies button not found in the UI")

        # Interact with elements
        try:
            accept_cookies_button.click()

            # Ensure UI updates - for simplicity, we'll check if cookies button is not visible
            WebDriverWait(driver, 20).until(
                EC.invisibility_of_element_located((By.ID, "rcc-confirm-button"))
            )
        except:
            self.fail("Clicking Accept cookies button caused an error in the UI")

if __name__ == "__main__":
    unittest.main()