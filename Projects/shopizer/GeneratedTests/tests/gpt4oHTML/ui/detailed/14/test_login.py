import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check structural elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))

            self.assertTrue(header.is_displayed(), "Header is not visible")
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
        except:
            self.fail("Header or Footer is missing")

        # Check presence and visibility of input fields and buttons in the login page
        driver.get("http://localhost/login")

        try:
            input_email = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            input_password = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            button_login = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

            self.assertTrue(input_email.is_displayed(), "Email input field is not visible")
            self.assertTrue(input_password.is_displayed(), "Password input field is not visible")
            self.assertTrue(button_login.is_displayed(), "Login button is not visible")
        except:
            self.fail("Email input, Password input or Login button is missing in the Login Page.")

        # Check navigation links
        try:
            nav_home = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            nav_tables = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            nav_chairs = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            nav_login = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            nav_register = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))

            self.assertTrue(nav_home.is_displayed(), "Home navigation link is not visible")
            self.assertTrue(nav_tables.is_displayed(), "Tables navigation link is not visible")
            self.assertTrue(nav_chairs.is_displayed(), "Chairs navigation link is not visible")
            self.assertTrue(nav_login.is_displayed(), "Login navigation link is not visible")
            self.assertTrue(nav_register.is_displayed(), "Register navigation link is not visible")
        except:
            self.fail("One or more navigation links are missing")

        # Interact with UI elements and confirm response
        try:
            button_login.click()
            # Wait for error message or successful login indicator (based on your application, adjust selectors)
            # Assuming there's an error or success message that appears on wrong login details
            # This part needs to be adjusted based on the actual outcome expected
            alert_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".react-toast-notifications__container")))

            self.assertTrue(alert_box.is_displayed(), "Page did not react visually on Login button click")
        except:
            self.fail("Did not properly interact with Login button or no visual feedback shown.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()