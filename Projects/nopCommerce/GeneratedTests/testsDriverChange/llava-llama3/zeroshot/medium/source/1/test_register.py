Here is a possible Python code for the Selenium test:
```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.element import ElementFinder

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        # Step 1: Open the homepage
        self.wait.until(EC.url_contains("http://max/"))

        # Step 2: Click the "Register"
        register_button = ElementFinder((By.XPATH, "//a[@class='button-1 register-continue-button']"))
        register_button.click()

        # Step 3: Wait for the registration page to load
        self.wait.until(EC.url_contains("http://max/register"))

        # Step 4: Fill all the fields
        gender_field = ElementFinder((By.XPATH, "//label[@for='gender-1']/following::input[1]"))
        gender_field.select_by_value('F')

        first_name_field = ElementFinder((By.XPATH, "//label[@for='FirstName']/following::input[1]"))
        first_name_field.send_keys("Test")
        last_name_field = ElementFinder((By.XPATH, "//label[@for='LastName']/following::input[1]"))
        last_name_field.send_keys("User")
        email_field = ElementFinder((By.XPATH, "//label[@for='Email']/following::input[1]"))
        email_field.send_keys("test@email.com")
        phone_number_field = ElementFinder((By.XPATH, "//label[@for='phone']/following::input[1]"))
        phone_number_field.send_keys("1234567890")
        package_name_field = ElementFinder((By.XPATH, "//label[@id='package-name']"))
        package_name_field.send_keys("TestPackage")
        price_field = ElementFinder((By.XPATH, "//label[@id='price']"))
        price_field.send_keys("1000")
        if self.wait.until(EC.element_to_be_clickable(register_button)):
            register_button.click()

        # Step 6: Verify that a message like "Your registration completed" is shown after successful registration
        register_result_message = ElementFinder((By.XPATH, "//div[@class='result']"))
        self.wait.until(EC.visibility_of_element_located(register_result_message))
        self.assertTrue(register_result_message.text == "Your registration completed")

if __name__ == '__main__':
    unittest.main()
```
This code uses the Selenium WebDriver to interact with the website. It first imports the necessary modules, then sets up a Chrome driver and defines a WebDriverWait object for waiting 20 seconds before interacting with elements.

The test\_registration method simulates the registration process as described in the task statement. It fills all the fields and submits the form. Finally, it checks that the message "Your registration completed" is shown after successful registration.

Finally, the code calls unittest.main() to run the test.
```
`-- 4.2.21 -- - 2021-04-02 09:47:38
```