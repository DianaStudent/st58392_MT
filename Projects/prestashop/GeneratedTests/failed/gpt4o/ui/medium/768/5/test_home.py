from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestDemoPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver

        # Wait for the page header
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )
        except Exception as e:
            self.fail(f"Header not found or visible: {e}")

        # Check navigation links
        nav_links = [
            (By.LINK_TEXT, "Clothes"),
            (By.LINK_TEXT, "Accessories"),
            (By.LINK_TEXT, "Art"),
            (By.LINK_TEXT, "Sign in"),
            (By.LINK_TEXT, "Create account"),
        ]

        for link_text, by_selector in nav_links:
            try:
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((by_selector, link_text))
                )
            except Exception as e:
                self.fail(f"Navigation link '{link_text}' not found or visible: {e}")

        # Verify banner is visible
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a.banner > img"))
            )
        except Exception as e:
            self.fail(f"Banner not found or visible: {e}")

        # Verify search input
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search our catalog']"))
            )
        except Exception as e:
            self.fail(f"Search input not found or visible: {e}")

        # Interact with a button and verify UI update
        try:
            button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".wishlist-button-add"))
            )
            button.click()
            # Assuming interaction causes a modal or UI change
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "wishlist-modal"))
            )
        except Exception as e:
            self.fail(f"Wishlist interaction failed or modal did not appear: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()