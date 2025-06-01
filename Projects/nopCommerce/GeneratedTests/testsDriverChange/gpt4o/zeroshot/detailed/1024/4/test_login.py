import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('http://max/')

    def tearDown(self):
        self.driver.quit()

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the home page and click the "Login" button
        login_menu_selector = (By.XPATH, "//ul[@class='top-menu notmobile']//li/a[contains(@href, '/customer/info')]")
        login_menu_element = wait.until(EC.presence_of_element_located(login_menu_selector))
        login_menu_element.click()

        # Wait until the login page loads fully
        login_page_title_selector = (By.XPATH, "//div[@class='page-title']/h1[text()='Welcome, Please Sign In!']")
        login_page_title_element = wait.until(EC.presence_of_element_located(login_page_title_selector))
        
        if not login_page_title_element:
            self.fail("Login page did not load.")

        # Fill in the email and password fields
        email_selector = (By.ID, "Email")
        email_element = wait.until(EC.presence_of_element_located(email_selector))
        email_element.send_keys("admin@admin.com")

        password_selector = (By.ID, "Password")
        password_element = wait.until(EC.presence_of_element_located(password_selector))
        password_element.send_keys("admin")

        # Click the login button
        login_button_selector = (By.XPATH, "//button[contains(@class, 'login-button')]")
        login_button_element = wait.until(EC.element_to_be_clickable(login_button_selector))
        login_button_element.click()

        # Verify the "Log out" button is present in the top navigation
        logout_menu_selector = (By.XPATH, "//a[contains(@href, '/logout')]")
        try:
            logout_menu_element = wait.until(EC.presence_of_element_located(logout_menu_selector))
            if not logout_menu_element or not logout_menu_element.is_displayed():
                self.fail("Log out button not present or visible.")
        except Exception:
            self.fail("Log out button not found.")

if __name__ == "__main__":
    unittest.main()