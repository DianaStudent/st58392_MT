from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(html_data["home_before_login"])

    def test_login(self):
        # Click the "Login" link.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login?returnurl=%2F']"))).click()

        # Wait for the login page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "main")))

        # Enter the email and password.
        email_input = self.driver.find_element(By.NAME, "Email")
        email_input.send_keys("admin@admin.com")

        password_input = self.driver.find_element(By.NAME, "Password")
        password_input.send_keys("admin")

        # Click the login button to submit the form
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-1 login-button']"))).click()

        # Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        logout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        self.assertTrue(logout_button.is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()