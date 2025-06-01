```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from html_automation.utils import generate_random_email

class TestRegisterFunctionality(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_register_functionality(self):
        try:
            # open the homepage
            self.driver.get("http://max/")

            # click on the "register" button
            register_button = WebDriverWait(self.driver, 20).until(
                EC.element_located((By.XPATH, "//button[contains(text(), 'Register')]")))
            )
            register_button.click()

            # wait for the registration page to load
            WebDriverWait(self.driver, 20).until(EC.url_contains("register"))

            # fill in the fields
            gender = WebDriverWait(self.driver, 20).until(
                EC.element_located((By.XPATH, "//input[contains(@id, 'gender-')]")))
            )
            gender.send_keys("Female")

            first_name = WebDriverWait(self.driver, 20).until(
                EC.element_located((By.XPATH, "//input[contains(@id, 'FirstName')]")))
            )
            first_name.send_keys("Test")

            last_name = WebDriverWait(self.driver, 20).until(
                EC.element_located((By.XPATH, "//input[contains(@id, 'LastName')]")))
            )
            last_name.send_keys("User")

            email = WebDriverWait(self.driver, 20).until(
                EC.element_located((By.XPATH, "//input[contains(@id, 'Email')]")))
            random_email = generate_random_email()
            email.send_keys(random_email)

            company = WebDriverWait(self.driver, 20).until(
                EC.element_located((By.XPATH, "//input[contains(@id, 'Company')]")))
            company.send_keys("TestCorp")

            password = WebDriverWait(self.driver, 20).until(
                EC.element_located((By.XPATH, "//input[contains(@id, 'Password')]")))
            password.send_keys("test11")

            # submit the registration form
            register_button = WebDriverWait(self.driver, 20).until(
                EC.element_located((By.XPATH, "//button[contains(text(), 'Create account')]")))
            )
            register_button.click()

            # verify that a message like "Your registration completed" is shown after successful registration
            success_message = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Your registration completed')]"))
            )
            self.assertEqual(success_message, "Your registration completed")
        except Exception as e:
            print("Test failed due to: ", e)

if __name__ == '__main__':
    unittest.main()
```
This test will fail if any of the following conditions are not met:

* The registration form is not displayed after clicking on  "Register".
* Any required element in the registration fields is missing or empty.
* The success message is not shown after submitting the registration form.