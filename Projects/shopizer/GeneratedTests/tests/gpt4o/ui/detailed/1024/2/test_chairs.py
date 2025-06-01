import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestShopizerPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check for header
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check for navigation menu
        nav_menu = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "main-menu")))
        self.assertTrue(nav_menu.is_displayed(), "Navigation menu is not visible")

        # Check for Home link
        home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        self.assertTrue(home_link.is_displayed(), "Home link is not visible")

        # Check for Tables link
        tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")
        
        # Check for Chairs link
        chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")

        # Check for footer
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check for language dropdown
        language_dropdown = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "language-style")))
        self.assertTrue(language_dropdown.is_displayed(), "Language dropdown is not visible")

        # Check for accept cookies button
        accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")

        # Click accept cookies button
        accept_cookies_button.click()

        # Check for login link
        login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        self.assertTrue(login_link.is_displayed(), "Login link is not visible")

        # Check for register link
        register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()