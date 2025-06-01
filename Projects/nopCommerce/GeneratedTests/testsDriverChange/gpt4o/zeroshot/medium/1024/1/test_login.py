import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page and click "My account"
        login_link = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ul[@class='top-menu notmobile']/li/a[@href='/customer/info']")))
        login_link.click()

        # Step 2: Wait for the login page to load
        page_title = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='page-title']/h1")))
        if not page_title or page_title.text != "Welcome, Please Sign In!":
            self.fail("Login page did not load properly.")

        # Step 3: Enter email and password
        email_input = driver.find_element(By.ID, "Email")
        password_input = driver.find_element(By.ID, "Password")
        
        if not email_input or email_input.get_attribute("type") != "email":
            self.fail("Email input field is not present or invalid.")
        if not password_input or password_input.get_attribute("type") != "password":
            self.fail("Password input field is not present or invalid.")
        
        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")

        # Step 4: Click the login button
        login_button = driver.find_element(By.XPATH, "//button[@class='button-1 login-button']")
        login_button.click()

        # Step 5: Verify that the user is logged in by checking for "Log out" button
        try:
            log_out_button = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(text(), 'Log out')]")))
            if not log_out_button:
                self.fail("Login failed, 'Log out' button not found.")
        except:
            self.fail("Login failed, 'Log out' button check threw an exception.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()