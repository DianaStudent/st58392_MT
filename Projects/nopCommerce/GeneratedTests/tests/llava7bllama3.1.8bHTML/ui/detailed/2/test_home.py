import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestMax(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")

    def test_max_elements_visible(self):
        # Wait for structural elements to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))

        # Check presence and visibility of input fields, buttons, labels, and sections
        elements = [
            ("username_input", By.NAME, "username"),
            ("email_input", By.NAME, "email"),
            ("password_input", By.NAME, "password"),
            ("login_button", By.XPATH, "//button[@type='submit']"),
            ("search_bar", By.ID, "search-bar"),
            ("search_button", By.ID, "search-button")
        ]

        for name, locator_type, locator in elements:
            element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((locator_type, locator)))
            self.assertEqual(element.is_displayed(), True)

    def test_max_interact_with_key_elements(self):
        # Interact with key UI elements
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()