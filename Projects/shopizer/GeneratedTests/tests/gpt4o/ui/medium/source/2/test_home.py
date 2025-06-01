import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver

        # Check navigation links
        nav_links_ids = [
            (By.LINK_TEXT, "Home"),
            (By.LINK_TEXT, "Tables"),
            (By.LINK_TEXT, "Chairs")
        ]
        for nav_id in nav_links_ids:
            element = self.wait.until(EC.visibility_of_element_located(nav_id))
            self.assertTrue(element.is_displayed(), f"Navigation link {nav_id} is not visible")

        # Check header elements
        header_elements = [
            (By.CSS_SELECTOR, "header.header-area"),
            (By.CSS_SELECTOR, "div.logo img"),
            (By.CSS_SELECTOR, "button.account-setting-active"),
            (By.CSS_SELECTOR, "button.icon-cart")
        ]
        for header in header_elements:
            element = self.wait.until(EC.visibility_of_element_located(header))
            self.assertTrue(element.is_displayed(), f"Header element {header} is not visible")

        # Check footer elements
        footer_elements = [
            (By.CSS_SELECTOR, "footer.footer-area"),
            (By.CSS_SELECTOR, "div.footer-logo img"),
            (By.LINK_TEXT, "Contact"),
            (By.LINK_TEXT, "Login"),
            (By.LINK_TEXT, "Register")
        ]
        for footer in footer_elements:
            element = self.wait.until(EC.visibility_of_element_located(footer))
            self.assertTrue(element.is_displayed(), f"Footer element {footer} is not visible")

        # Check main content area
        main_content_elements = [
            (By.CSS_SELECTOR, "div.site-blocks-cover"),
            (By.CSS_SELECTOR, "div.section-title-5"),
            (By.LINK_TEXT, "Shop Now"),
            (By.CSS_SELECTOR, "div.product-wrap-2")
        ]
        for content in main_content_elements:
            element = self.wait.until(EC.visibility_of_element_located(content))
            self.assertTrue(element.is_displayed(), f"Main content element {content} is not visible")

        # Interact with the "Accept Cookies" button
        accept_cookies_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        accept_cookies_btn.click()

        # Verify UI update
        self.assertFalse(
            self.is_element_present(By.ID, "rcc-confirm-button"),
            "Cookies consent button should be gone after clicking"
        )

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except:
            return False
        return True

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()