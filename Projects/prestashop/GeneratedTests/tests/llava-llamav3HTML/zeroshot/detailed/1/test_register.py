```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from time import sleep

class TestRegisterUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_register_user(self):
        # Step 1: Open the homepage.
        self.driver.get("http://www.example.com")
        print("Step 1 passed")

        # Step 2: Click the login link from the top navigation.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text()='No account? Create one here')]")))
        self.driver.find_element_by_xpath("//*[contains(text_='No account? Create one here')]").click()
        print("Step 2 passed")

        # Step 3: Fill in the following fields using credentials.
        gender = self.driver.find_element_by_name("gender")
        self.assertEqual(gender.get_attribute("data-name"), "male")
        gender.send_keys(1)
        self.assertEqual(gender.get_attribute("class"), "form-control")

        first_name = self.driver.find_element_by_name("first\_name")
        self.assertEqual(first\_name.get\_attribute("data-name"), "Test")
        first\_name.send\_keys("Test")
        self.assertEqual(first\_name.get\_attribute("class"), "form-control")

        last\_name = self.driver.find\_element\_by\_name("last\_name")
        self.assertEqual(last\_name.get\_attribute("data-name"), "User")
        last\_name.send\_keys("User")
        self.assertEqual(last\_name.get\_attribute("class"), "form-control")

        email = self.driver.find\_element\_by\_name("email")
        self.assertEqual(email.get\_attribute("data-name"), "test\_\_\_\_@user.com")
        self.assertEqual(email.get\_attribute("class"), "form-control")
```