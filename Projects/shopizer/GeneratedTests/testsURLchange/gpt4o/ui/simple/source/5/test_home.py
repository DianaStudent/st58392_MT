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
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver

        # Wait for elements to be present and visible
        wait = WebDriverWait(driver, 20)

        # Check the header logo is present
        header_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo a img")))
        if not header_logo:
            self.fail("Header logo not found.")

        # Check for main navigation links
        nav_links = [
            ("Home", "/"),
            ("Tables", "/category/tables"),
            ("Chairs", "/category/chairs")
        ]

        for link_text, href in nav_links:
            link = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[text()='{link_text}' and @href='{href}']")))
            self.assertTrue(link, f"Navigation link for {link_text} not found.")

        # Check the 'Accept cookies' button
        accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        if not accept_cookies_button:
            self.fail("Accept cookies button not found.")

        # Check the login and register links
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        if not login_link:
            self.fail("Login link not found.")

        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        if not register_link:
            self.fail("Register link not found.")

        # Check for the search input field in subscription section
        subscribe_email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.email[type='email']")))
        if not subscribe_email_input:
            self.fail("Subscribe email input not found.")

        # Check for the subscribe button
        subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button")))
        if not subscribe_button:
            self.fail("Subscribe button not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()