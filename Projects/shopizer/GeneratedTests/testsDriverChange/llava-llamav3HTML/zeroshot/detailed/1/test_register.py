import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.actions.interaction import Key
from selenium.webdriver.common.actions.interaction import InteractionCommands
import time

class TestRegistration(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        try:
            # 1. Open the home page.
            self.driver.get("http://localhost/")

            # 2. Click on the account icon/button.
            WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_tag_name('button').clickable())
            )

            # 3. Select the "Register" option.
            registration_button = self.driver.find_element_by_tag_name('button')
            registration_button.click()

            # Wait for the registration page to load.
            time.sleep(10)

            # 4. Fill in all fields: email, password, repeat password, first name, last name.
            email_input = self.driver.find_element_by_name("email")
            password_input = self.driver.find_element_by_name("currentPassword")
            repeat_password_input = self.driver.find_element_by_name("repeatPassword")
            first_name_input = self.driver.find_element_by_name("firstname")
            last_name_input = self.driver.find_element_by_name("lastname")

            email_input.clear()
            password_input.clear()
            repeat_password_input.clear()
            first_name_input.clear()
            last_name_input.clear()

            # Generate a dynamic email address for testing
            email_address = "test_" + str(time.time()) + "@user.com"
            self.driver.find_element_by_name("email").send_keys(email_address)

            password_input.send_keys("test**11")
            repeat_password_input.send_keys("test**11")

            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")

            # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
            countries_dropdown = self.driver.find_element_by_id('data-countries')
            select_country = Select(countries_dropdown)
            select_country.select_by_visible_text('Country Name')

            time.sleep(10)

            regions_states_dropdown = WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_id('data-regions-states'))
            select_state = Select(regions_states_dropdown)
            select_country = Select(countries_dropdown)
            select_country.select_by_visible_text("Country Name")
            time.sleep(10)
            select_state.select_by_visible_text('State Name')

            # 7. Submit the form.
            self.driver.find_element_by_name("submit").click()

            # Wait for the page to redirect and confirm registration success by:
            # checking if the URL contains "/my-account" in the URL.
            time.sleep(10)
            self.assertTrue(
                self.driver.current_url().contains("/my-account"),
                "Registration failed: unable to access account management page."
            )

        except Exception as e:
            print(f"An error occurred during registration: {e}")