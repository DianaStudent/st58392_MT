import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alerts import Alert
from selenium.webdriver.common.touch_actions import TouchAction
from selenium.webdriver.common.touch_action_builder import TouchActionBuilder
from selenium.webdriver.common.touch_input import TouchInput
from selenium.webdriver.common.touch_input_builder import TouchInputBuilder
from selenium.webdriver.common.touch_output import TouchOutput
from selenium.webdriver.common.touch_output_builder import TouchOutputBuilder

class TestRegister(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "path/to/chromedriver"
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        self.driver.get("http://localhost/")
        # Click on the account icon/buttion
        account_button = WebDriverWait(self.driver, 20).until(
            visibility_of_element_located((By.XPATH, "//a[contains(text(), 'account')]"))
        )
        self.driver.execute_script(f"arguments[0].click();", account_button)

        # Select the registration option
        register_button = WebDriverWait(self.driver, 20).until(
            visibility_of_element_located((By.XPATH, "//a[contains(text(), 'register')]"))
        )
        self.driver.execute_script(f"arguments[0].click();", register_button)

        # Wait for the registration page to load
        WebDriverWait(self.driver, 20).until(
            visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Register now')]"))
        )

        # Fill in all fields: email, password, repeat password, first name, last name.
        email_field = WebDriverWait(self.driver, 20).until(
            visibility_of_element_located((By.XPATH, "//input[@name='email']"))
        )
        self.driver.execute_script(f"arguments[0].value={f'test_{self.random.randint(100000)}@user.com'};")

        password_field = WebDriverWait(self.driver, 20).until(
            visibility_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        self.driver.execute_script(f"arguments[0].value={f'password{self.random.randint(10000000)}';")

        repeat_password_field = WebDriverWait(self.driver, 20).until(
            visibility_of_element_located((By.XPATH, "//input[@name='repeatPassword']"))
        )
        self.driver.execute_script(f"arguments[0].value={f'password{self.random.randint(10000000)}';")

        first_name_field = WebDriverWait(self.driver, 20).until(
            visibility_of_element_located((By.XPATH, "//input[@name='firstName']"))
        )
        self.driver.execute_script(f"arguments[0].value={f'{self.random.randint(100000)}';")

        last_name_field = WebDriverWait(self.driver, 20).until(
            visibility_of_element_located((By.XPATH, "//input[@name='lastName']"))
        )
        self.driver.execute_script(f"arguments[0].value={f'{self.random.randint(100000)}';")

        # Select a first country
        country_select = WebDriverWait(self.driver, 20).until(
            visibility_of_element_located((By.XPATH, "//select[contains(@id, 'country')][1]"))
        )
        country_index = self.random.randint(10)
        self.driver.execute_script(f"arguments[0].selectedIndex={country_index};")

        # Select a first state
        state_select = WebDriverWait(self.driver, 20).until(
            visibility_of_element_located((By.XPATH, "//select[contains(@id, 'state')][1]"))
        )
        country = self.country_names[country_index]
        self.country = country
        state_index = self.random.randint(len(country[country]))
        self.country = country[state_index]
        self.driver.execute_script(f"arguments[0].selectedIndex={state_index};")

        # Submit the form
        submit_button = WebDriverWait(self.driver, 20).until(
            visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Register now')]"))
        )
        self.driver.execute_script(f"arguments[0].click();")

        # Wait for the page to redirect and confirm registration success by:
        # checking if the URL contains "/my-account"
        WebDriverWait(self.driver, 20).until(
            expected_condition=ExpectedConditions.url_to_contain("/my-account"),
            time=20,
            timeout=10
        )

    @property
    def random(self):
        return randint(1000000)

    @property
    def country_names(self):
        country_names = {
            '1': ['United States', 'Canada', 'Australia'],
            '2': ['Germany', 'France', 'Italy'],
            '3': ['China', 'Japan', 'Brazil']
        }
        return list(country_names.keys())

def main():
    test = TestRegister()
    test.test_register()

if __name__ == "__main__":
    unittest.main()