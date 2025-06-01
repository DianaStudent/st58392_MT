import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check for the presence of logo
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-logo img"))), "Logo is not visible")

        # Check for navigation links
        links = ["/", "/newproducts", "/search", "/customer/info", "/blog", "/contactus"]
        for link in links:
            link_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul[@class='top-menu notmobile']//a[@href='{link}']")))
            self.assertTrue(link_element.is_displayed(), f"Navigation link {link} is not visible")

        # Check for "Register" and "Log in" button
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.register-button"))), "Register button is not visible")
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.login-button"))), "Log in button is not visible")

        # Check for email and password input fields
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "Email"))), "Email input field is not visible")
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "Password"))), "Password input field is not visible")

        # Interact with the login button to check for UI changes
        login_button = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button")
        login_button.click()

        # Verify that error messages appear when inputs are empty
        error_message_email = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-valmsg-for='Email']")))
        error_message_password = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-valmsg-for='Password']")))
        
        self.assertTrue(error_message_email.is_displayed(), "Email error message is not visible after submitting")
        self.assertTrue(error_message_password.is_displayed(), "Password error message is not visible after submitting")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()