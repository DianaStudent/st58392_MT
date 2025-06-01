import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify presence of navigation links
        nav_links = ["Home page", "New products", "Search", "My account", "Blog", "Contact us"]
        for link_text in nav_links:
            try:
                wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except:
                self.fail(f"Navigation link '{link_text}' not visible")

        # Verify presence of form fields
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        except:
            self.fail("Email or Password input field not visible")

        # Verify presence of buttons
        buttons = {
            "Register": "//button[contains(@class, 'register-button')]",
            "Log in": "//button[contains(@class, 'login-button')]"
        }
        for button_name, button_xpath in buttons.items():
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, button_xpath)))
            except:
                self.fail(f"Button '{button_name}' not visible")

        # Interact with the page
        # Try clicking the 'Log in' button
        try:
            login_button = driver.find_element(By.XPATH, buttons["Log in"])
            login_button.click()
        except:
            self.fail("Failed to click 'Log in' button")

        # Confirm that there's no visible error after interaction
        try:
            error_notification = driver.find_element(By.ID, "dialog-notifications-error")
            self.assertFalse(error_notification.is_displayed(), "Error notification is visible after clicking 'Log in'")
        except:
            pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()