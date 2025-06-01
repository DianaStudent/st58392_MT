import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#_desktop_logo img")))
            self.assertTrue(logo.is_displayed(), "Logo is not visible.")
        except Exception:
            self.fail("Logo is not present on the page.")

        # Verify contact us link
        try:
            contact_us = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
            self.assertTrue(contact_us.is_displayed(), "Contact us link is not visible.")
        except Exception:
            self.fail("Contact us link is not present on the page.")

        # Verify language selector
        try:
            language_selector = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".language-selector button")))
            self.assertTrue(language_selector.is_displayed(), "Language selector is not visible.")
        except Exception:
            self.fail("Language selector is not present on the page.")

        # Verify sign in link
        try:
            sign_in = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertTrue(sign_in.is_displayed(), "Sign in link is not visible.")
        except Exception:
            self.fail("Sign in link is not present on the page.")

        # Verify cart icon
        try:
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart")))
            self.assertTrue(cart_icon.is_displayed(), "Cart icon is not visible.")
        except Exception:
            self.fail("Cart icon is not present on the page.")

        # Verify search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_widget input[name='s']")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible.")
        except Exception:
            self.fail("Search input is not present on the page.")

        # Verify footer newsletter label
        try:
            newsletter_label = wait.until(EC.visibility_of_element_located((By.ID, "block-newsletter-label")))
            self.assertTrue(newsletter_label.is_displayed(), "Newsletter label is not visible.")
        except Exception:
            self.fail("Newsletter label is not present on the page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()