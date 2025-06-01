from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to login page
        my_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
        my_account_link.click()

        # Input email
        email_input = wait.until(EC.element_to_be_clickable((By.ID, "Email")))
        email_input.send_keys("admin@admin.com")

        # Input password
        password_input = driver.find_element(By.ID, "Password")
        password_input.send_keys("admin")

        # Click login button
        login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
        login_button.click()

        # Confirm success by checking the presence of "Administration" link
        try:
            admin_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Administration")))
        except:
            self.fail("Log in failed - 'Log out' or 'Administration' link not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()