import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header links
        header_links = [
            "/register?returnUrl=%2F",
            "/login?returnUrl=%2F",
            "/wishlist",
            "/cart",
            "/",
            "/newproducts",
            "/search",
            "/customer/info",
            "/blog",
            "/contactus"
        ]
        for link in header_links:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
            self.assertTrue(element.is_displayed(), f"Link {link} is not visible")

        # Verify Login Form elements
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        self.assertTrue(email_input.is_displayed(), "Email input is not visible")

        password_input = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        self.assertTrue(password_input.is_displayed(), "Password input is not visible")

        login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))
        self.assertTrue(login_button.is_displayed(), "Login button is not visible")

        # Interact with elements - e.g., click login
        login_button.click()

        # Verify Error message (expected due to lack of credentials)
        # Assuming there should be an error element
        error_notification = wait.until(EC.visibility_of_element_located((By.ID, "dialog-notifications-error")))
        self.assertTrue(error_notification.is_displayed(), "Error notification is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()