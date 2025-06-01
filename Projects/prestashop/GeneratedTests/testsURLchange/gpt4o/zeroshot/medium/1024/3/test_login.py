import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

class MyStoreLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver

        # Wait for and click on the sign-in link
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a/span[text()='Sign in']"))
            )
            sign_in_link.click()
        except NoSuchElementException:
            self.fail("Sign in link not found.")

        # Wait for the login form to appear
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )
            password_field = driver.find_element(By.ID, "field-password")
        except NoSuchElementException:
            self.fail("Email or password field not found.")

        # Fill in credentials
        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # Submit the form
        try:
            submit_button = driver.find_element(By.ID, "submit-login")
            submit_button.click()
        except NoSuchElementException:
            self.fail("Submit button not found.")

        # Verify login success
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]/span[text()='Sign out']"))
            )
            self.assertTrue(sign_out_link.is_displayed(), "Login failed, Sign out link not visible.")
        except NoSuchElementException:
            self.fail("Sign out link not found, login may have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()