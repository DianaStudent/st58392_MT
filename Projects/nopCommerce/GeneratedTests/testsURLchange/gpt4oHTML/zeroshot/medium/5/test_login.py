import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")  # Replace with actual home page URL

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the home page
        home_page_url = "http://max/"  # Replace with actual home page URL
        driver.get(home_page_url)

        # Click the "Login" link in the header menu
        try:
            login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
            if login_link and login_link.text.strip() == "My account":
                login_link.click()
            else:
                self.fail("Login link not found in the header menu.")
        except:
            self.fail("Login link not found or not clickable.")

        # Wait for the login page to load
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.page-title h1")))
        except:
            self.fail("Login page did not load correctly.")

        # Enter the email
        try:
            email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
            if email_input:
                email_input.clear()
                email_input.send_keys("admin@admin.com")
            else:
                self.fail("Email input field not found.")
        except:
            self.fail("Email input field not found or not interactable.")

        # Enter the password
        try:
            password_input = wait.until(EC.presence_of_element_located((By.ID, "Password")))
            if password_input:
                password_input.clear()
                password_input.send_keys("admin")
            else:
                self.fail("Password input field not found.")
        except:
            self.fail("Password input field not found or not interactable.")

        # Click the login button to submit the form
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button")
            if login_button:
                login_button.click()
            else:
                self.fail("Login button not found.")
        except:
            self.fail("Login button not found or not clickable.")

        # Verify that the user is logged in by checking the "Log out" button
        try:
            logout_link = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Log out")))
            if not logout_link:
                self.fail("Log out button not found, login might have failed.")
        except:
            self.fail("Log out button not found, login might have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()