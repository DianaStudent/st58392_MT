from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLoginSimple(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() # Update the driver based on your chrome version
        self.driver.get("http://localhost:8080/en/")

    def test_login_simple(self):
        try:
            email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-name='email']")))
            email_input.send_keys("test@user.com")
            
            password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-name='password']")))
            password_input.send_keys("test@user1")

            login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            login_button.click()

            sign_out_text = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Sign out')]")))

        except Exception as e:
            self.fail("Test failed due to: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()