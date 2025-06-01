from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopizerUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        
    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)  # Timeout after 20 seconds

        # Check header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
            self.assertTrue(header.is_displayed())
        except:
            self.fail("Header not found or visible")

        # Check navigation links
        try:
            nav_links = wait.until(EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, "nav ul li a")
            ))
            self.assertTrue(all(link.is_displayed() for link in nav_links))
        except:
            self.fail("Navigation links not found or visible")

        # Check main content
        try:
            shop_area = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.shop-area")))
            self.assertTrue(shop_area.is_displayed())
        except:
            self.fail("Shop area not found or visible")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
            self.assertTrue(footer.is_displayed())
        except:
            self.fail("Footer not found or visible")

        # Check cookie consent button and interact
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_cookies_button.is_displayed())
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button not found or clickable")

        # Verify that the UI reacts visually (e.g., cookie consent disappears)
        try:
            cookie_consent = driver.find_element(By.CSS_SELECTOR, "div.CookieConsent")
            self.assertFalse(cookie_consent.is_displayed())
        except:
            pass  # No element is acceptable if it disappears

        # Verify all required elements
        required_selectors = [
            "input.email",
            "button.scroll-top",
            "div.product-wrap",
            "div.breadcrumb-area",
        ]

        for selector in required_selectors:
            try:
                element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
                self.assertTrue(element.is_displayed())
            except:
                self.fail(f"Element with selector '{selector}' is missing or not visible")

if __name__ == "__main__":
    unittest.main()