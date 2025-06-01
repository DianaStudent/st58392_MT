import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check the presence of header
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check the presence of footer
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check the presence of navigation
        nav = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'main-menu')))
        self.assertTrue(nav.is_displayed(), "Navigation is not visible")

        # Check input fields, buttons, sections
        self.check_element_visibility(By.ID, "rcc-confirm-button", "Accept cookies button is not visible")
        self.check_element_visibility(By.LINK_TEXT, "English", "Language dropdown is not visible")
        self.check_element_visibility(By.LINK_TEXT, "Home", "Home link is not visible")
        self.check_element_visibility(By.LINK_TEXT, "Tables", "Tables link is not visible")
        self.check_element_visibility(By.LINK_TEXT, "Chairs", "Chairs link is not visible")
        self.check_element_visibility(By.LINK_TEXT, "Login", "Login link is not visible")
        self.check_element_visibility(By.LINK_TEXT, "Register", "Register link is not visible")

        # Interact with specific elements
        accept_cookies_button = driver.find_element(By.ID, "rcc-confirm-button")
        accept_cookies_button.click()

        # Confirm interaction effect
        self.assertTrue(header.is_displayed(), "Header should still be visible after interaction")

    def check_element_visibility(self, by_method, selector, error_message):
        element = self.wait.until(EC.visibility_of_element_located((by_method, selector)))
        self.assertTrue(element.is_displayed(), error_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()