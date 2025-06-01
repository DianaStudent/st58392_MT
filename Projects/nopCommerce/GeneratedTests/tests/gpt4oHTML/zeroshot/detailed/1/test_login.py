import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://your_test_site.com")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver

        # Wait for home page to load and check presence of "My account" link
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
        except:
            self.fail("The 'My account' link is not present on the home page.")

        # Clicking the "My account" to navigate to login
        driver.find_element(By.LINK_TEXT, "My account").click()

        # Wait for login page to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "page-title"))
            )
        except:
            self.fail("The login page did not load successfully.")

        # Enter Email
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Email"))
        )
        if not email_input:
            self.fail("Email input field is not present.")
        email_input.clear()
        email_input.send_keys("admin@admin.com")

        # Enter Password
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Password"))
        )
        if not password_input:
            self.fail("Password input field is not present.")
        password_input.clear()
        password_input.send_keys("admin")

        # Click login button
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
        )
        login_button.click()

        # Verify login success by checking presence of "Administration" link
        try:
            admin_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "administration"))
            )
            if not admin_link:
                self.fail("Login failed, 'Administration' link not found.")
        except:
            self.fail("Login failed, 'Administration' link not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()