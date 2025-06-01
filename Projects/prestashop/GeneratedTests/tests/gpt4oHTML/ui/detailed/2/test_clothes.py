import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITestCase(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header is visible
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")
        except Exception as e:
            self.fail(f"Header not found: {e}")

        # Verify footer is visible
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
        except Exception as e:
            self.fail(f"Footer not found: {e}")

        # Verify navigation links are visible
        try:
            nav_links = {"home": "http://localhost:8080/en/",
                         "clothes": "http://localhost:8080/en/3-clothes",
                         "accessories": "http://localhost:8080/en/6-accessories",
                         "art": "http://localhost:8080/en/9-art"}

            for link_text, url in nav_links.items():
                link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text.capitalize())))
                self.assertEqual(link.get_attribute('href'), url, f"{link_text} link URL is incorrect")
                self.assertTrue(link.is_displayed(), f"{link_text} link is not visible")
        except Exception as e:
            self.fail(f"Navigation links not found: {e}")

        # Verify input fields and buttons
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            self.assertTrue(search_input.is_displayed(), "Search input field is not visible")

            sign_in_button = self.wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Sign in")))
            self.assertTrue(sign_in_button.is_displayed(), "Sign in button is not visible")

            cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
            self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

        except Exception as e:
            self.fail(f"Input fields or buttons not found: {e}")

        # Verify sections
        try:
            category_header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "h1")))
            self.assertTrue(category_header.is_displayed(), "Category header is not visible")

        except Exception as e:
            self.fail(f"Sections not found: {e}")

        # Interact with some UI elements
        try:
            sign_in_button.click()
            self.wait.until(EC.url_contains("login"))
            self.assertIn("login", driver.current_url, "Failed to navigate to login page after clicking sign in")
        except Exception as e:
            self.fail(f"Interaction with UI elements failed: {e}")

    def tearDown(self):
        # Clean up and close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()