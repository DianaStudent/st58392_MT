import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        self.driver.get("http://max/login?returnUrl=%2F")

        # Check navigation links
        nav_links = [
            "//a[text()='Home page']",
            "//a[text()='New products']",
            "//a[text()='Search']",
            "//a[text()='My account']",
            "//a[text()='Blog']",
            "//a[text()='Contact us']"
        ]
        for link in nav_links:
            self.assertTrue(
                self.is_element_present_and_visible(By.XPATH, link),
                f"Navigation link {link} is missing or not visible"
            )

        # Check input fields
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        self.assertTrue(email_input.is_displayed(), "Email input is not visible")
        self.assertTrue(password_input.is_displayed(), "Password input is not visible")

        # Check buttons
        login_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))
        register_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))
        self.assertTrue(login_button.is_displayed(), "Login button is not visible")
        self.assertTrue(register_button.is_displayed(), "Register button is not visible")

        # Interact with an element and check UI update
        login_button.click()

        # Verify no error occurred after the click
        self.assertTrue(self.is_element_present_and_visible(By.CLASS_NAME, "login-page"), "UI error after login button click")

    def is_element_present_and_visible(self, by, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            return True
        except:
            return False

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()