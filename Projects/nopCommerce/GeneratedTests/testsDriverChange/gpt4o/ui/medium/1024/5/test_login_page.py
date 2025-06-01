import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class WebPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check if navigation links are visible
        navigation_links = [
            (By.LINK_TEXT, "Home page"),
            (By.LINK_TEXT, "New products"),
            (By.LINK_TEXT, "Search"),
            (By.LINK_TEXT, "My account"),
            (By.LINK_TEXT, "Blog"),
            (By.LINK_TEXT, "Contact us")
        ]

        for link in navigation_links:
            element = wait.until(EC.visibility_of_element_located(link))
            if not element.is_displayed():
                self.fail(f"{link[1]} link is not visible")

        # Check if login form fields are visible
        try:
            email_field = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            password_field = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))

            if not (email_field.is_displayed() and password_field.is_displayed() and login_button.is_displayed()):
                self.fail("Login form fields are not visible")
        except:
            self.fail("Required login form fields are missing")

        # Check Register button
        try:
            register_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))

            if not register_button.is_displayed():
                self.fail("Register button is not visible")
        except:
            self.fail("Register button is missing")

        # Click Register button and verify navigation
        register_button.click()
        wait.until(EC.url_contains("register"))

        # Check that UI updates correctly (e.g., the URL changes)
        current_url = driver.current_url
        if "register" not in current_url:
            self.fail("Clicking Register did not navigate to the register page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()