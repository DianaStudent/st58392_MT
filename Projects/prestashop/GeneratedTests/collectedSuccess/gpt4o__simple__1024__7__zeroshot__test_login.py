import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:8080/en/"

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)

        try:
            # Click on the "Sign in" link
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()

            # Enter email
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_input.clear()
            email_input.send_keys("test@user.com")

            # Enter password
            password_input = driver.find_element(By.ID, "field-password")
            password_input.clear()
            password_input.send_keys("test@user1")

            # Submit the form
            submit_button = driver.find_element(By.ID, "submit-login")
            submit_button.click()

            # Confirm success by checking for "Sign out"
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign out"))
            )

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()