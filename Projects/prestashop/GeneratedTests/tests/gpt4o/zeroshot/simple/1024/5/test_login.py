import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # or webdriver.Firefox() or any other browser driver
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on the Sign in link
        sign_in_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
        )
        sign_in_link.click()

        # Enter Email
        email_input = wait.until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        email_input.send_keys("test@user.com")

        # Enter Password
        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        # Click Sign in button
        sign_in_button = driver.find_element(By.ID, "submit-login")
        sign_in_button.click()

        # Check that "Sign out" link is present indicating login was successful
        try:
            sign_out_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertTrue(sign_out_link.is_displayed())
        except:
            self.fail("Sign out link not found. Login may have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()