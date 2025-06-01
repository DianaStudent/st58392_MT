import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Find and click the "My account" link
        try:
            my_account_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to click 'My account' link: {e}")
            return

        # Find and click the "Register" link
        try:
            register_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Failed to click 'Register' link: {e}")
            return

        # Wait for the registration page to load
        try:
            wait.until(EC.presence_of_element_located((By.ID, "register-button")))
        except Exception as e:
            self.fail(f"Registration page did not load correctly: {e}")
            return

        # Fill in the registration form
        try:
            female_radio = wait.until(EC.element_to_be_clickable((By.ID, "gender-female")))
            female_radio.click()
        except:
            self.fail("Could not click the female gender radio button")
            return

        try:
            first_name_input = driver.find_element(By.ID, "FirstName")
            first_name_input.send_keys("Test")
        except:
            self.fail("Could not find or interact with the first name input field")
            return

        try:
            last_name_input = driver.find_element(By.ID, "LastName")
            last_name_input.send_keys("User")
        except:
            self.fail("Could not find or interact with the last name input field")
            return

        email = "testuser" + str(int(time.time())) + "@example.com"
        try:
            email_input = driver.find_element(By.ID, "Email")
            email_input.send_keys(email)
        except:
            self.fail("Could not find or interact with the email input field")
            return

        try:
            company_input = driver.find_element(By.ID, "Company")
            company_input.send_keys("TestCorp")
        except:
            self.fail("Could not find or interact with the company input field")
            return

        try:
            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("test11")
        except:
            self.fail("Could not find or interact with the password input field")
            return

        try:
            confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password_input.send_keys("test11")
        except:
            self.fail("Could not find or interact with the confirm password input field")
            return

        # Submit the form
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except:
            self.fail("Could not find or interact with the register button")
            return

        # Verify registration success
        try:
            result_element = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            )
            result_text = result_element.text
            self.assertIn("Your registration completed", result_text)
        except Exception as e:
            self.fail(f"Registration verification failed: {e}")

if __name__ == "__main__":
    unittest.main()