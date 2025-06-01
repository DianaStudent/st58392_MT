import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # 1. Verify structure elements are visible
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header, "Header is missing.")

            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertIsNotNone(footer, "Footer is missing.")

            nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
            self.assertIsNotNone(nav, "Navigation is missing.")
        except Exception as e:
            self.fail(f"Structure elements test failed: {str(e)}")

        # 2. Check presence and visibility of key UI elements (input fields, buttons, labels, sections)
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible.")

            contact_link = wait.until(EC.visibility_of_element_located((
                By.LINK_TEXT, "Contact us")))
            self.assertTrue(contact_link.is_displayed(), "Contact us link is not visible.")

            sign_in_link = wait.until(EC.visibility_of_element_located((
                By.LINK_TEXT, "Sign in")))
            self.assertTrue(sign_in_link.is_displayed(), "Sign in link is not visible.")

            products_section = wait.until(EC.visibility_of_element_located((By.ID, "products")))
            self.assertTrue(products_section.is_displayed(), "Products section is not visible.")

            # Example of checking a button interaction
            filter_button = wait.until(EC.element_to_be_clickable((By.ID, "search_filter_toggler")))
            self.assertTrue(filter_button.is_displayed(), "Filter button is not visible.")
            filter_button.click()

        except Exception as e:
            self.fail(f"UI element presence test failed: {str(e)}")

        # 3. Check page reacts to UI interactions
        try:
            # Example of UI interaction result verification
            filter_controls = wait.until(EC.visibility_of_element_located((By.ID, "search_filter_controls")))
            self.assertTrue(filter_controls.is_displayed(), "Filter controls are not visible after clicking filter button.")
        
        except Exception as e:
            self.fail(f"UI interaction test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()