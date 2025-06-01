from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class StoreUITests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def check_element_present_and_visible(self, by, identifier, element_name):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, identifier)))
            self.assertTrue(element.is_displayed(), f"{element_name} is not visible.")
        except:
            self.fail(f"{element_name} element is not found or not visible.")

    def test_main_ui_components(self):
        # Check header components
        self.check_element_present_and_visible(By.CSS_SELECTOR, ".header", "Header")
        self.check_element_present_and_visible(By.CSS_SELECTOR, ".header-links", "Header Links")
        self.check_element_present_and_visible(By.CSS_SELECTOR, ".header-logo", "Header Logo")

        # Check presence and visibility of login page elements
        self.check_element_present_and_visible(By.CSS_SELECTOR, ".page-title > h1", "Login Page Title")
        self.check_element_present_and_visible(By.ID, "Email", "Email Field")
        self.check_element_present_and_visible(By.ID, "Password", "Password Field")
        self.check_element_present_and_visible(By.CSS_SELECTOR, ".button-1.login-button", "Log in Button")
        
        # Check footer components
        self.check_element_present_and_visible(By.CSS_SELECTOR, ".footer", "Footer")
        self.check_element_present_and_visible(By.CSS_SELECTOR, ".footer-upper", "Footer Upper Section")

        # Check navigation links
        self.check_element_present_and_visible(By.LINK_TEXT, "Home page", "Home Page Link")
        self.check_element_present_and_visible(By.LINK_TEXT, "My account", "My Account Link")
        self.check_element_present_and_visible(By.LINK_TEXT, "Contact us", "Contact Us Link")

if __name__ == "__main__":
    unittest.main()