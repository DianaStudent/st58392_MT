import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost/login')
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check for logo presence
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))
            self.assertTrue(logo.is_displayed())
        except:
            self.fail("Logo not visible")

        # Check for navigation links
        expected_links = ["/", "/category/tables", "/category/chairs"]
        nav_links = driver.find_elements(By.CSS_SELECTOR, ".main-menu nav ul li a")
        self.assertEqual(len(nav_links), len(expected_links))

        for link, expected in zip(nav_links, expected_links):
            self.assertEqual(link.get_attribute('href'), 'http://localhost' + expected)

        # Check for login form fields
        try:
            email_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_field = driver.find_element(By.NAME, "loginPassword")
            self.assertTrue(email_field.is_displayed() and password_field.is_displayed())
        except:
            self.fail("Login form fields not visible")

        # Check for login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, ".button-box > button[type='submit']")
            self.assertTrue(login_button.is_displayed())
        except:
            self.fail("Login button not visible")

        # Interact with an element: Click the 'Accept Cookies' button
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button interaction failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()