import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        # Verify logo presence and visibility
        logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))
        self.assertIsNotNone(logo, "Logo is missing or not visible.")

        # Verify navigation links
        nav_links = ["Home", "Tables", "Chairs"]
        for link_text in nav_links:
            link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertIsNotNone(link, f"Navigation link '{link_text}' is missing or not visible.")

        # Verify login tab is active
        login_tab = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav-link.active")))
        self.assertIsNotNone(login_tab, "Login tab is missing or not active.")

        # Verify input fields
        username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        self.assertIsNotNone(username_input, "Username input is missing or not visible.")
        
        password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
        self.assertIsNotNone(password_input, "Password input is missing or not visible.")

        # Verify login button
        login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span='Login']")))
        self.assertIsNotNone(login_button, "Login button is missing or not visible.")

        # Interact with 'Accept Cookies' button
        accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertIsNotNone(accept_cookies_button, "'Accept cookies' button is missing or not visible.")
        accept_cookies_button.click()

        # After clicking, the button should no longer be visible
        self.wait.until(EC.invisibility_of_element_located((By.ID, "rcc-confirm-button")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()