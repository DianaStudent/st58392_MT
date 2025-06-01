import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebpageUITestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        # Verify header elements
        header_links = ['Home', 'Tables', 'Chairs']
        for link in header_links:
            element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link)))
            self.assertTrue(element.is_displayed(), f'{link} link is not visible')

        # Verify navigation to Login/Register forms
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertTrue(login_link.is_displayed(), 'Login link is not visible')
        self.assertTrue(register_link.is_displayed(), 'Register link is not visible')

        # Verify form fields for registration
        form_fields = ['Email address', 'Password', 'Repeat Password', 'First Name', 'Last Name', 'State']
        for placeholder in form_fields:
            element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"input[placeholder='{placeholder}']")))
            self.assertTrue(element.is_displayed(), f'{placeholder} input is not visible')

        # Verify Register button
        register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']")))
        self.assertTrue(register_button.is_displayed(), 'Register button is not visible')

    def test_interactive_element(self):
        driver = self.driver
        wait = self.wait

        # Interact - Click Accept on Cookie Consent
        cookie_accept_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        self.assertTrue(cookie_accept_button.is_displayed(), 'Cookie consent button is not visible')
        
        cookie_accept_button.click()

        # Verify cookie banner disappeared
        with self.assertRaises(Exception):
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".CookieConsent")))

        # Interact - Switch to Register tab
        register_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.nav-link.active")))
        register_tab.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()