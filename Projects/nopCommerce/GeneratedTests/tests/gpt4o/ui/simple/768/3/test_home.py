import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class VerifyUIElementsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header elements
        header_links_selector = ".header-links a"
        try:
            header_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, header_links_selector)))
            self.assertGreater(len(header_links), 0, "Header links are not visible")
        except:
            self.fail(f"Header links not found using selector {header_links_selector}")

        # Verify search box
        search_box_selector = "#small-search-box-form"
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, search_box_selector)))
            self.assertTrue(search_box.is_displayed(), "Search box is not visible")
        except:
            self.fail(f"Search box not found using selector {search_box_selector}")

        # Verify top menu links
        top_menu_selector = ".top-menu.notmobile a"
        try:
            top_menu_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, top_menu_selector)))
            self.assertGreater(len(top_menu_links), 0, "Top menu links are not visible")
        except:
            self.fail(f"Top menu links not found using selector {top_menu_selector}")

        # Verify footer links
        footer_links_selector = ".footer-upper a"
        try:
            footer_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, footer_links_selector)))
            self.assertGreater(len(footer_links), 0, "Footer links are not visible")
        except:
            self.fail(f"Footer links not found using selector {footer_links_selector}")

        # Verify newsletter subscription input and button
        newsletter_input_selector = "#newsletter-email"
        newsletter_button_selector = "#newsletter-subscribe-button"
        try:
            newsletter_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, newsletter_input_selector)))
            newsletter_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, newsletter_button_selector)))
            self.assertTrue(newsletter_input.is_displayed(), "Newsletter input is not visible")
            self.assertTrue(newsletter_button.is_displayed(), "Newsletter subscribe button is not visible")
        except:
            self.fail(f"Newsletter elements not found using selectors {newsletter_input_selector} or {newsletter_button_selector}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()