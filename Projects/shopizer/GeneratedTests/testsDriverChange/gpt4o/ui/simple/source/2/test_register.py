import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header logo
        header_logo = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='logo']/a/img")))
        self.assertTrue(header_logo.is_displayed(), "Header logo is not visible")

        # Check navigation links
        nav_links = wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, "//div[@class='main-menu']//a")))
        self.assertEqual(len(nav_links), 3, "Navigation links are missing or incorrect")        

        # Check login/register buttons
        login_register_buttons = wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, "//div[@class='account-dropdown']//a")))
        self.assertEqual(len(login_register_buttons), 2, "Login/Register buttons are missing or incorrect")

        # Check form fields
        form_fields = [
            {"name": "email", "placeholder": "Email address"},
            {"name": "password", "placeholder": "Password"},
            {"name": "repeatPassword", "placeholder": "Repeat Password"},
            {"name": "firstName", "placeholder": "First Name"},
            {"name": "lastName", "placeholder": "Last Name"},
            {"name": "stateProvince", "placeholder": "State"}
        ]

        for field in form_fields:
            form_field = wait.until(EC.visibility_of_element_located(
                (By.XPATH, f"//input[@name='{field['name']}' and @placeholder='{field['placeholder']}']")))
            self.assertTrue(form_field.is_displayed(), f"Form field {field['name']} is not visible")

        # Check select country dropdown
        country_dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//select")))
        self.assertTrue(country_dropdown.is_displayed(), "Country dropdown is not visible")

        # Check register button
        register_button = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//button[.//span[text()='Register']]")))
        self.assertTrue(register_button.is_displayed(), "Register button is not visible")

        # Check footer address
        footer_address = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='footer-widget']//a[contains(text(), '1234 Street address')]")))
        self.assertTrue(footer_address.is_displayed(), "Footer address is not visible")

        # Check footer links
        footer_links = wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, "//div[@class='footer-list']//a")))
        self.assertGreaterEqual(len(footer_links), 3, "Footer links are missing or insufficient")

if __name__ == "__main__":
    unittest.main()