import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_check_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Checking for header, footer, and navigation visibility
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
            breadcrumb = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'breadcrumb-area')))
        except:
            self.fail("Essential structural components are missing or not visible.")

        # Checking presence of input fields and buttons
        try:
            username_input = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'loginPassword')))
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Login']")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
        except:
            self.fail("Required input fields or buttons are missing or not visible.")

        # Interacting with elements
        try:
            username_input.send_keys("test@example.com")
            password_input.send_keys("password")
            login_button.click()
        except:
            self.fail("Unable to interact with the input fields or submit button.")

        # Confirmation of visual UI reaction
        try:
            login_page = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'login-register-wrapper')))
        except:
            self.fail("UI did not react as expected upon form submission.")

        # Asserting that all elements have been found and are visible
        self.assertTrue(header.is_displayed())
        self.assertTrue(footer.is_displayed())
        self.assertTrue(breadcrumb.is_displayed())
        self.assertTrue(login_page.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()