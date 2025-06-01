```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

class TestAppspaceLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_login_with_valid_credentials(self):
        driver = self.driver
        driver.get("http://localhost:8080/")

        email_field = driver.find_element_by_name("email")
        password_field = driver.find_element_by_name("password")

        email_field.send_keys("example@email.com")
        password_field.send_keys("example_password")

        login_button = driver.find_element_by_name("sign_in")

        self.wait.until(EC.element_to_be_clickable(login_button))
        login_button.click()

    def test_register(self):
        driver = self.driver
        driver.get("http://localhost:8080/registration")

        first_name_field = driver.find_element_by_name("first_name")
        last_name_field = driver.find_element_by_name("last_name")

        select_state = Select(driver.find_element_by_name("state"))
        for option in select_state.options:
            if option.text == "California":
                select_state.select_by_visible_text(option.text)
                break

        address1_field = driver.find_element_by_name("address_1")
        city_field = driver.find_element_by_name("city")

        zip_code_field = driver.find_element_by_name("zip_code")
        phone_number_field = driver.find_element_by_name("phone_number")

        submit_button = driver.find_element_by_name("register")

        self.wait.until(EC.element_to_be_clickable(submit_button))
        submit_button.click()

if __name__ == '__main__':
    unittest.main()
```