import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.url = "http://max/"
        self.email = f"testuser{int(time.time())}@example.com"

    def test_registration(self):
        driver = self.driver
        driver.get(self.url)

        # Click the "Register" link
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except:
            self.fail("Register link not found")

        # Wait for the registration form to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "form[action='/register?returnurl=%2F']"))
            )
        except:
            self.fail("Registration form did not load")

        # Select gender
        try:
            female_radio = driver.find_element(By.ID, "gender-female")
            female_radio.click()
        except:
            self.fail("Female gender radio button not found")

        # Fill in required fields
        try:
            driver.find_element(By.ID, "FirstName").send_keys("Test")
            driver.find_element(By.ID, "LastName").send_keys("User")
            driver.find_element(By.ID, "Email").send_keys(self.email)
            driver.find_element(By.ID, "Company").send_keys("TestCorp")
            driver.find_element(By.ID, "Password").send_keys("test11")
            driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")
        except:
            self.fail("Failed to fill in all required fields")

        # Submit the registration form
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except:
            self.fail("Register button not found or not clickable")

        # Wait for the response page
        try:
            result_text = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".result"))
            )
            self.assertIn("Your registration completed", result_text.text)
        except:
            self.fail("Registration confirmation message not found or incorrect")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()