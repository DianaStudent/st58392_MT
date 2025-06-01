import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for header
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(header, "Header is missing")

        # Check for main menu items
        menu_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".main-menu ul li a")))
        expected_menu_texts = ["Home", "Tables", "Chairs"]
        actual_menu_texts = [item.text for item in menu_items]
        for text in expected_menu_texts:
            self.assertIn(text, actual_menu_texts, f"Menu item {text} is missing")

        # Check for input fields
        input_fields = {
            "email": "input[name='email']",
            "password": "input[name='password']",
            "repeat_password": "input[name='repeatPassword']",
            "first_name": "input[name='firstName']",
            "last_name": "input[name='lastName']",
            "state": "input[name='stateProvince']"
        }
        for name, selector in input_fields.items():
            element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            self.assertIsNotNone(element, f"Input field {name} is missing")

        # Check for buttons
        register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        self.assertIsNotNone(register_button, "Register button is missing")

        # Check footer
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        self.assertIsNotNone(footer, "Footer is missing")

        # Interact with cookies consent button
        try:
            consent_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            consent_button.click()
        except Exception:
            self.fail("Cookies consent button is missing or not clickable")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()