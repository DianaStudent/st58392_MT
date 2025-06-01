import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebPageUI(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")
            
            # Check footer
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")

            # Check navigation links
            links = ["Home", "Tables", "Chairs"]
            for link_text in links:
                link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertTrue(link.is_displayed(), f"Link '{link_text}' is not visible")

            # Check login and register links
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            self.assertTrue(login_link.is_displayed(), "Login link is not visible")

            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(register_link.is_displayed(), "Register link is not visible")

            # Check subscribe section
            subscribe_section = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "subscribe-area-3")))
            self.assertTrue(subscribe_section.is_displayed(), "Subscribe section is not visible")

            # Check input field and button in subscribe section
            email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
            self.assertTrue(email_input.is_displayed(), "Email input is not visible")

            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".clear-3.dark-red-subscribe .button")))
            self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible")

            # Interact with UI elements
            subscribe_button.click()
            # Check for visual feedback (e.g., toast notification or other UX feedback)
            # Add assertions here if there's known feedback to expect

        except Exception as e:
            self.fail(f"UI element check failed: {str(e)}")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()