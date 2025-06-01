import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class DemoPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = self.wait

        # Verify header elements
        headers = [
            (By.CSS_SELECTOR, "#_desktop_logo .logo"),
            (By.CSS_SELECTOR, ".header-nav .container .right-nav #_desktop_contact_link"),
            (By.CSS_SELECTOR, ".header-top-right #_desktop_top_menu"),
            (By.CSS_SELECTOR, ".header-nav .right-nav #_desktop_language_selector"),
            (By.CSS_SELECTOR, ".header-nav .right-nav #_desktop_user_info a"),
            (By.CSS_SELECTOR, ".header-nav .right-nav #_desktop_cart .header")
        ]

        for header in headers:
            element = wait.until(EC.visibility_of_element_located(header))
            if element is None:
                self.fail(f"Header element {header} is not visible.")

        # Verify main carousel
        carousel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#carousel")))
        if carousel is None:
            self.fail("Carousel is not visible.")

        # Verify product list
        products = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".featured-products .products")))
        if products is None:
            self.fail("Product list is not visible.")

        # Verify footer elements
        footer = [
            (By.CSS_SELECTOR, ".js-footer .block_newsletter "),
            (By.CSS_SELECTOR, ".js-footer .block-social"),
            (By.CSS_SELECTOR, ".js-footer .footer-container .container")
        ]

        for footer_element in footer:
            element = wait.until(EC.visibility_of_element_located(footer_element))
            if element is None:
                self.fail(f"Footer element {footer_element} is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()