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
        self.driver.maximize_window()
        self.base_url = "http://max/"

    def test_ui_components(self):
        driver = self.driver
        driver.get(self.base_url + '/register?returnUrl=%2F')

        # Wait for the header to be visible
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'header'))
        )
        self.assertIsNotNone(header, "Header is missing.")

        # Wait for the footer to be visible
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'footer'))
        )
        self.assertIsNotNone(footer, "Footer is missing.")

        # Check navigation menu
        nav_menu = driver.find_elements(By.CSS_SELECTOR, '.top-menu a')
        self.assertGreater(len(nav_menu), 0, "Navigation menu items are missing.")
        for menu_item in nav_menu:
            self.assertTrue(menu_item.is_displayed(), f"Menu item {menu_item.text} is not visible.")

        # Ensure all required form fields are present and visible
        form_fields = [
            ("id", "gender-male"),
            ("id", "gender-female"),
            ("id", "FirstName"),
            ("id", "LastName"),
            ("id", "Email"),
            ("id", "Password"),
            ("id", "ConfirmPassword"),
            ("id", "register-button")
        ]

        for selector_type, selector_value in form_fields:
            field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((getattr(By, selector_type.upper()), selector_value))
            )
            self.assertIsNotNone(field, f"Form field with {selector_type} '{selector_value}' is missing.")

        # Check for specific buttons existence
        register_button = driver.find_element(By.ID, 'register-button')
        self.assertTrue(register_button.is_displayed(), "Register button is not visible.")

        # Interact with register button
        register_button.click()

        # Confirm form submission interaction causes an effect (for demo, check a visible section)
        notification_area = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'bar-notification'))
        )
        self.assertTrue(notification_area.is_displayed(), "Notification area did not appear after form submission attempt.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()