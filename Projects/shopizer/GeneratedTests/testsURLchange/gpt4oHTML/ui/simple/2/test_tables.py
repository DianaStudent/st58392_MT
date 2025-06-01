import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_components(self):
        driver = self.driver

        # Check Header
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header-area')))
        if not header.is_displayed():
            self.fail("Header is not visible.")

        # Check Navigation Links
        nav_links = self.verify_nav_links()
        for link_text, element in nav_links.items():
            if not element.is_displayed():
                self.fail(f"Navigation link '{link_text}' is not visible.")

        # Check Cookie Consent Banner
        cookie_banner = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.CookieConsent')))
        if not cookie_banner.is_displayed():
            self.fail("Cookie consent banner is not visible.")
        
        # Check Accept Cookies Button
        accept_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        if not accept_button.is_displayed():
            self.fail("Accept cookies button is not visible.")

        # Check Product Listing
        products = self.verfiy_products()
        for product_name, product_element in products.items():
            if not product_element.is_displayed():
                self.fail(f"Product '{product_name}' is not visible.")

        # Check Footer
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.footer-area')))
        if not footer.is_displayed():
            self.fail("Footer is not visible.")

    def verify_nav_links(self):
        return {
            "Home": self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home'))),
            "Tables": self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables'))),
            "Chairs": self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs'))),
            "Login": self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Login'))),
            "Register": self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
        }
        
    def verfiy_products(self):
        return {
            "Olive Table": self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Olive Table"))),
            "Chair": self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chair"))),
            "Chair Beige": self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chair Beige"))),
            "Genuine Chair": self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Genuine Chair")))
        }

if __name__ == "__main__":
    unittest.main()