import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        
        # Wait for header elements (Home, Tables, Chairs) to be visible
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

        # Wait for and interact with the language dropdown
        language_dropdown = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "language-style"))
        )
        self.assertTrue(language_dropdown.is_displayed())

        # Wait for and click accept cookies button
        accept_cookies_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        )
        accept_cookies_button.click()

        # Verify login form elements
        login_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
        )
        login_link.click()

        # Wait for login form to be visible
        email_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        password_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "loginPassword"))
        )
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[span='Login']"))
        )

        self.assertTrue(email_input.is_displayed())
        self.assertTrue(password_input.is_displayed())
        self.assertTrue(login_button.is_displayed())

        # Check no UI errors when interacting with Login button
        login_button.click()

if __name__ == "__main__":
    unittest.main()