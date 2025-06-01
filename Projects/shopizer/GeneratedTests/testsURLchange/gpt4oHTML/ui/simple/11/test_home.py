import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UIElementsTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver

        try:
            # Check presence and visibility of header/logo
            header_logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo a img")))
            self.assertTrue(header_logo.is_displayed())

            # Check presence and visibility of navigation menu links
            nav_links = ["Home", "Tables", "Chairs"]
            for nav_text in nav_links:
                nav_item = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, nav_text)))
                self.assertTrue(nav_item.is_displayed())
            
            # Check presence and visibility of cookie consent button
            cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookie_button.is_displayed())

            # Check presence and visibility of product items
            product_img = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-wrap-2 .product-img a img")))
            self.assertTrue(product_img.is_displayed())

            # Check presence and visibility of footer links
            footer_links = ["Contact", "Login", "Register"]
            for link_text in footer_links:
                footer_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertTrue(footer_link.is_displayed())

            # Check presence and visibility of newsletter subscription input box
            newsletter_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form-3 .mc-form .email")))
            self.assertTrue(newsletter_input.is_displayed())
        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()