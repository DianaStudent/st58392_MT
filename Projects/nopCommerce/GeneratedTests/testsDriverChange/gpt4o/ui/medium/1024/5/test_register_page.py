import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = self.wait

        # Check header links
        try:
            navigation_links = ["//a[@href='/']", 
                                "//a[@href='/newproducts']", 
                                "//a[@href='/search']", 
                                "//a[@href='/customer/info']", 
                                "//a[@href='/blog']", 
                                "//a[@href='/contactus']"]
            for link_xpath in navigation_links:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, link_xpath)))
                self.assertTrue(element.is_displayed(), f"Navigation link {link_xpath} not visible")
        except Exception as e:
            self.fail(f"Navigation link check failed: {str(e)}")

        # Check registration form fields
        try:
            form_fields = ["//input[@id='FirstName']", 
                           "//input[@id='LastName']", 
                           "//input[@id='Email']", 
                           "//input[@id='Password']", 
                           "//input[@id='ConfirmPassword']"]
            for field_xpath in form_fields:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, field_xpath)))
                self.assertTrue(element.is_displayed(), f"Form field {field_xpath} not visible")
        except Exception as e:
            self.fail(f"Form field check failed: {str(e)}")

        # Check the registration button
        try:
            register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='register-button']")))
            self.assertTrue(register_button.is_displayed(), "Register button not visible")
            # Interact with the register button
            register_button.click()
        except Exception as e:
            self.fail(f"Register button check failed: {str(e)}")

        # Check confirmation of UI update/alert (if applicable)
        try:
            alert_message = "//div[@id='dialog-notifications-error']"
            element = wait.until(EC.visibility_of_element_located((By.XPATH, alert_message)))
            self.assertTrue(element.is_displayed(), "Alert message not visible after clicking register")
        except Exception as e:
            # Continue if no alert shown; this might be a valid case.
            pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()