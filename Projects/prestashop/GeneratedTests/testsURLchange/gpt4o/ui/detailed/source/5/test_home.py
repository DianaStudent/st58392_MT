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
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Check header visibility
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header, "Header is not visible.")

            # Check footer visibility
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertIsNotNone(footer, "Footer is not visible.")

            # Check main navigation visibility
            nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
            self.assertIsNotNone(nav, "Main navigation is not visible.")

            # Check presence of search input field
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            self.assertIsNotNone(search_input, "Search input field is not visible.")

            # Check presence of 'Sign in' button
            sign_in_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertIsNotNone(sign_in_button, "Sign in button is not visible.")
            
            # Check 'Contact us' link visibility
            contact_us_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
            self.assertIsNotNone(contact_us_link, "Contact us link is not visible.")

            # Check visibility of 'Popular Products' section
            popular_products_section = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "featured-products")))
            self.assertIsNotNone(popular_products_section, "Popular Products section is not visible.")
            
            # Interaction: Click on 'Sign in' button
            sign_in_button.click()

            # Confirm the UI reacts visually (e.g., redirected to login page)
            WebDriverWait(driver, 20).until(EC.url_contains("/login"))
            self.assertIn("login", driver.current_url, "Page did not navigate to login on Sign in button click.")

        except Exception as e:
            self.fail(f"A required UI element is missing or an interaction failed: {str(e)}")

if __name__ == "__main__":
    unittest.main(verbosity=2)