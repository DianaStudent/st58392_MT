from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_max_page_elements(self):
        # Navigate to the home page
        self.driver.get("http://max/")

        # Check that the main UI components are present and visible

        # Header
        header = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "header"))
        )
        self.assertIsNotNone(header)

        # Navigation Bar
        navigation_bar = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "navigation-bar"))
        )
        self.assertIsNotNone(navigation_bar)

        # Search Form
        search_form = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "search-form"))
        )
        self.assertIsNotNone(search_form)
        self.assertIn("Search", search_form.text)

        # Register Button
        register_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='register-button']"))
        )
        self.assertIsNotNone(register_button)
        self.assertEqual(register_button.text, "Register")

        # Login Link
        login_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "login-link"))
        )
        self.assertIsNotNone(login_link)
        self.assertEqual(login_link.text, "Login")

        # Search Input
        search_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "search-input"))
        )
        self.assertIsNotNone(search_input)

if __name__ == '__main__':
    unittest.main()