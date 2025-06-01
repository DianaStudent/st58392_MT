import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check navigation elements visibility
        nav_home = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
        nav_tables = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
        nav_chairs = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
        self.assertTrue(nav_home.is_displayed(), "Navigation link 'Home' is not visible")
        self.assertTrue(nav_tables.is_displayed(), "Navigation link 'Tables' is not visible")
        self.assertTrue(nav_chairs.is_displayed(), "Navigation link 'Chairs' is not visible")

        # Check login/register form elements visibility and interaction
        register_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@data-rb-event-key, 'register')]")))
        register_tab.click()

        email_input = self.wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
        password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
        repeat_password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, 'repeatPassword')))
        first_name_input = self.wait.until(EC.visibility_of_element_located((By.NAME, 'firstName')))
        last_name_input = self.wait.until(EC.visibility_of_element_located((By.NAME, 'lastName')))
        country_select = self.wait.until(EC.visibility_of_element_located((By.NAME, 'stateProvince')))
        register_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Register']")))

        self.assertTrue(email_input.is_displayed(), "Email input is not visible")
        self.assertTrue(password_input.is_displayed(), "Password input is not visible")
        self.assertTrue(repeat_password_input.is_displayed(), "Repeat Password input is not visible")
        self.assertTrue(first_name_input.is_displayed(), "First Name input is not visible")
        self.assertTrue(last_name_input.is_displayed(), "Last Name input is not visible")
        self.assertTrue(country_select.is_displayed(), "Country select is not visible")
        self.assertTrue(register_button.is_displayed(), "Register button is not visible")

        # Interact with accept cookies button
        try:
            accept_cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button is missing or not clickable")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()