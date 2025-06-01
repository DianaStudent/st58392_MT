import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header.header-area')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer.footer-area')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check navigation visibility
        nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav')))
        self.assertTrue(nav.is_displayed(), "Navigation is not visible")

        # Check login button in navigation
        login_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/login"]')))
        self.assertTrue(login_button.is_displayed(), "Login button is not visible")
        login_button.click()

        # Check login form fields
        username_field = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
        self.assertTrue(username_field.is_displayed(), "Username field is not visible")

        password_field = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'user-password')))
        self.assertTrue(password_field.is_displayed(), "Password field is not visible")

        # Check login form submit button
        submit_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]/span[text()="Login"]')))
        self.assertTrue(submit_button.is_displayed(), "Submit button is not visible")
        
        # Interact with 'Accept Cookies' button if present
        try:
            accept_cookies_button = driver.find_element(By.ID, 'rcc-confirm-button')
            if accept_cookies_button.is_displayed():
                accept_cookies_button.click()
        except:
            pass

        # Check presence of 'Register' link in login section
        register_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/register"]')))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()