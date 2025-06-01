import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header and footer visibility
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header')))
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.footer')))

            # Check presence and visibility of navigation links
            nav_links = ['Home page', 'New products', 'Search', 'My account', 'Blog', 'Contact us']
            for link_text in nav_links:
                self.assertTrue(driver.find_element(By.LINK_TEXT, link_text).is_displayed())

            # Check login form input fields
            email_input = wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
            password_input = wait.until(EC.visibility_of_element_located((By.ID, 'Password')))

            # Check buttons
            login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-button')))
            register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.register-button')))

            # Interact with email input
            email_input.send_keys("test@example.com")
            # Toggle password visibility
            driver.find_element(By.CSS_SELECTOR, '.password-eye').click()

            # Click login button
            login_button.click()

        except Exception as e:
            self.fail(f"UI element missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()