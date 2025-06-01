import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):

    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage. (Done in setUp)

        # 2. Click the login link from the top navigation.
        sign_in_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")))
        sign_in_link.click()

        # 3. Wait for the login page to load.
        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))

        # 4. Fill in the email and password fields.
        email_field.send_keys("test@user.com")
        password_field = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        password_field.send_keys("test@user1")

        # 5. Click the submit button.
        submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit-login")))
        submit_button.click()

        # 6. Wait for the redirect after login.
        sign_out_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")))

        # 7. Confirm that login was successful.
        # Check for "Sign out" link.
        if sign_out_link:
            sign_out_text = sign_out_link.text
            if sign_out_text and "Sign out" in sign_out_text:
                pass  # Success, "Sign out" is present
            else:
                self.fail("Sign out link text is incorrect or empty.")
        else:
            self.fail("Sign out link is not present after login.")

        # Check for the username.
        username_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span[@class='hidden-sm-down']")))
        if username_element:
            username_text = username_element.text
            if username_text and username_text != "":
                pass
            else:
                self.fail("Username text is empty.")
        else:
            self.fail("Username element is not present after login.")

if __name__ == "__main__":
    unittest.main()