from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://localhost/login")

        wait = WebDriverWait(driver, 20)

        try:
            # Check for navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Check form inputs
            username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))

            # Check buttons
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))

            # Interact with Accept Cookies button
            accept_cookies_button.click()

            # Example interaction: Try to click Login button and check no UI errors
            login_button.click()

            # Confirm elements exist without errors
            assert "Login" in driver.title

        except Exception as e:
            self.fail(f"Test scenario failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()