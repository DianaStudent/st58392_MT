from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver

        # Check header logo
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))
            self.assertTrue(logo.is_displayed())
        except:
            self.fail("Logo is not present or not visible.")

        # Check main menu links
        menu_links = [
            (By.LINK_TEXT, "Home"),
            (By.LINK_TEXT, "Tables"),
            (By.LINK_TEXT, "Chairs")
        ]

        for link_text, selector in menu_links:
            try:
                link = self.wait.until(EC.visibility_of_element_located(selector))
                self.assertTrue(link.is_displayed())
            except:
                self.fail(f"Menu link '{link_text}' is not present or not visible.")
        
        # Check buttons in the header
        button_selectors = [
            (By.CSS_SELECTOR, ".account-setting-active"),
            (By.CSS_SELECTOR, ".icon-cart"),
            (By.CSS_SELECTOR, ".mobile-aside-button")
        ]

        for idx, selector in enumerate(button_selectors):
            try:
                button = self.wait.until(EC.visibility_of_element_located(selector))
                self.assertTrue(button.is_displayed())
            except:
                self.fail(f"Header button {idx + 1} is not present or not visible.")
        
        # Check footer links
        footer_links = [
            (By.LINK_TEXT, "Contact"),
            (By.LINK_TEXT, "Login"),
            (By.LINK_TEXT, "Register")
        ]

        for link_text, selector in footer_links:
            try:
                link = self.wait.until(EC.visibility_of_element_located(selector))
                self.assertTrue(link.is_displayed())
            except:
                self.fail(f"Footer link '{link_text}' is not present or not visible.")
        
        # Check subscribe form
        try:
            subscribe_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form input[type='email']")))
            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form button")))
            self.assertTrue(subscribe_input.is_displayed())
            self.assertTrue(subscribe_button.is_displayed())
        except:
            self.fail("Subscribe form is not present or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()