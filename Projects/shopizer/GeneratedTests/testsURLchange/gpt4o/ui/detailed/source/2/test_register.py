import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'header.header-area')))
        except:
            self.fail("Header is not visible")

        # Check footer
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'footer.footer-area')))
        except:
            self.fail("Footer is not visible")

        # Check main navigation menu
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'nav ul')))
        except:
            self.fail("Main navigation is not visible")

        # Check Login form inputs
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.NAME, 'username')))
        except:
            self.fail("Username input is not visible")

        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.NAME, 'loginPassword')))
        except:
            self.fail("Password input is not visible")

        # Check Login button
        try:
            login_button = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//button/span[text()='Login']")))
        except:
            self.fail("Login button is not visible")

        # Interact with UI elements
        login_button.click()

        # Check for reaction in the UI (e.g. error message due to missing input)
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.login-form-container')))
        except:
            self.fail("Login form submission did not react as expected")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()