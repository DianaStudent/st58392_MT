import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header-area')))
        self.assertIsNotNone(header, "Header is missing")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.footer-area')))
        self.assertIsNotNone(footer, "Footer is missing")

        # Check navigation links visibility
        nav_links = ['Home', 'Tables', 'Chairs']
        for link_text in nav_links:
            self.assertTrue(driver.find_element(By.LINK_TEXT, link_text).is_displayed(), f"{link_text} link is missing")

        # Check login form elements
        driver.get("http://localhost/login")
        username_field = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
        self.assertTrue(username_field.is_displayed(), "Username field is missing")
      
        password_field = wait.until(EC.visibility_of_element_located((By.NAME, 'loginPassword')))
        self.assertTrue(password_field.is_displayed(), "Password field is missing")
      
        login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        self.assertTrue(login_button.is_displayed(), "Login button is missing")

        remember_me_checkbox = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@type="checkbox"]')))
        self.assertTrue(remember_me_checkbox.is_displayed(), "Remember Me checkbox is missing")

        forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Forgot Password?')))
        self.assertTrue(forgot_password_link.is_displayed(), "Forgot Password? link is missing")

        # Interact with Accept Cookies button
        accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        self.assertTrue(accept_cookies_button.is_displayed(), "Accept Cookies button is missing")
        accept_cookies_button.click()

    def test_register_form(self):
        driver = self.driver
        wait = self.wait

        # Navigate to register page and check the elements
        driver.get("http://localhost/register")
        email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
        self.assertTrue(email_field.is_displayed(), "Email field is missing")

        password_field = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
        self.assertTrue(password_field.is_displayed(), "Password field is missing")

        repeat_password_field = wait.until(EC.visibility_of_element_located((By.NAME, 'repeatPassword')))
        self.assertTrue(repeat_password_field.is_displayed(), "Repeat Password field is missing")

        first_name_field = wait.until(EC.visibility_of_element_located((By.NAME, 'firstName')))
        self.assertTrue(first_name_field.is_displayed(), "First Name field is missing")

        last_name_field = wait.until(EC.visibility_of_element_located((By.NAME, 'lastName')))
        self.assertTrue(last_name_field.is_displayed(), "Last Name field is missing")

        register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        self.assertTrue(register_button.is_displayed(), "Register button is missing")

if __name__ == "__main__":
    unittest.main()