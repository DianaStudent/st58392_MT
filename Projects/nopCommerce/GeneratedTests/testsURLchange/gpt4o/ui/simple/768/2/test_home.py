import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header elements
        header_elements = [
            (By.CSS_SELECTOR, ".ico-register"),
            (By.CSS_SELECTOR, ".ico-login"),
            (By.CSS_SELECTOR, ".ico-wishlist"),
            (By.CSS_SELECTOR, ".ico-cart"),
            (By.CSS_SELECTOR, ".header-logo a"),
            (By.CSS_SELECTOR, ".search-box-text"),
            (By.CSS_SELECTOR, ".search-box-button"),
            (By.CSS_SELECTOR, ".top-menu.notmobile"),
            (By.CSS_SELECTOR, ".swiper .swiper-slide img"),
            (By.CSS_SELECTOR, ".topic-block-title"),
            (By.CSS_SELECTOR, ".topic-block-body")
        ]

        for by, selector in header_elements:
            try:
                element = wait.until(EC.visibility_of_element_located((by, selector)))
                self.assertTrue(element.is_displayed(), f"Element {selector} is not visible")
            except Exception as e:
                self.fail(f"Element {selector} not found or not visible. Exception: {str(e)}")

        # Verify footer elements
        footer_elements = [
            (By.CSS_SELECTOR, ".footer-block.information"),
            (By.CSS_SELECTOR, ".footer-block.customer-service"),
            (By.CSS_SELECTOR, ".footer-block.my-account"),
            (By.CSS_SELECTOR, ".footer-block.follow-us"),
            (By.CSS_SELECTOR, ".newsletter-subscribe-button")
        ]

        for by, selector in footer_elements:
            try:
                element = wait.until(EC.visibility_of_element_located((by, selector)))
                self.assertTrue(element.is_displayed(), f"Element {selector} is not visible")
            except Exception as e:
                self.fail(f"Element {selector} not found or not visible. Exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()