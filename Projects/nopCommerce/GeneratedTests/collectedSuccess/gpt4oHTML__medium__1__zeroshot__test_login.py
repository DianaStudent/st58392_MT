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
        self.driver.set_window_size(1920, 1080)  # Adjust according to the zoom level
        self.driver.get("http://max/")  # Replace with actual URL of the home page

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the home page and find "Login" link
        try:
            login_link = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='top-menu notmobile']/li/a[contains(text(), 'My account')]")))
            login_link.click()
        except:
            self.fail("Login link not found on the home page")

        # Wait for the login page to load and find the email field
        try:
            email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
            password_field = driver.find_element(By.ID, "Password")
        except:
            self.fail("Email or Password field not found on the login page")

        # Enter credentials
        email_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        # Find and click the login button
        try:
            login_button = driver.find_element(By.XPATH, "//button[@class='button-1 login-button']")
            login_button.click()
        except:
            self.fail("Login button not found on the login page")

        # Verify the user is logged in by checking the presence of "Log out" button
        try:
            log_out_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='admin-header-links']/a[@class='administration']")))
            self.assertTrue(log_out_button.is_displayed(), "Log out button not displayed, login failed")
        except:
            self.fail("Log out button not found post login")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()