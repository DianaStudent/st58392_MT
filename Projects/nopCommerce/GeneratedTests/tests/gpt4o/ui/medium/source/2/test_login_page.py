import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://max/login?returnUrl=%2F")
    
    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header elements
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))

            # Check logo
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-logo")))

            # Check search form
            wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))

            # Check navigation menu
            menu_items = ["Home page", "New products", "Search", "My account", "Blog", "Contact us"]
            for item in menu_items:
                wait.until(EC.visibility_of_element_located((By.LINK_TEXT, item)))

            # Check login form elements
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))

            # Interact with login button
            login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "login-button")))
            login_button.click()

            # Verify no UI error occurs (assume error div is displayed when there's an error)
            error_notification = driver.find_element(By.ID, "dialog-notifications-error")
            self.assertFalse(error_notification.is_displayed(), "Login click leads to error notification.")

        except Exception as e:
            self.fail(f"UI Element check failed: {str(e)}")

if __name__ == "__main__":
    unittest.main()