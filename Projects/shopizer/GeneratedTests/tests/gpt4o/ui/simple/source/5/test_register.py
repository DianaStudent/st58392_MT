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

    def test_ui_elements(self):
        driver = self.driver
        
        # Verify header elements
        try:
            header_logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo a img")))
            self.assertTrue(header_logo.is_displayed(), "Logo is not visible")
            
            navigation_links = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.main-menu nav ul")))
            self.assertTrue(navigation_links.is_displayed(), "Navigation links are not visible")
        
        except Exception as e:
            self.fail(f"Header elements verification failed: {e}")

        # Verify form fields in login and register tabs
        try:
            login_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='login']")))
            register_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='register']")))
            
            self.assertTrue(login_tab.is_displayed(), "Login tab is not visible")
            self.assertTrue(register_tab.is_displayed(), "Register tab is not visible")
            
            # Switch to register form
            register_tab.click()

            register_email = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            register_password = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            register_repeat_password = self.wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
            
            self.assertTrue(register_email.is_displayed(), "Register email field is not visible")
            self.assertTrue(register_password.is_displayed(), "Register password field is not visible")
            self.assertTrue(register_repeat_password.is_displayed(), "Register repeat password field is not visible")

        except Exception as e:
            self.fail(f"Form fields verification failed: {e}")

        # Verify presence and visibility of buttons
        try:
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")
            
            register_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span='Register']")))
            self.assertTrue(register_button.is_displayed(), "Register button is not visible")
        
        except Exception as e:
            self.fail(f"Button elements verification failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()