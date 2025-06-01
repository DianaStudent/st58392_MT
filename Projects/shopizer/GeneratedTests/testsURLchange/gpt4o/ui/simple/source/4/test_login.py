import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost/')

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check for header elements
            header_logos = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//header//img")))
            self.assertTrue(len(header_logos) > 0, "Header logo not visible.")

            # Main navigation links
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//nav//a")))
            self.assertTrue(any(link.text == "Home" for link in nav_links), "Home link not visible.")
            self.assertTrue(any(link.text == "Tables" for link in nav_links), "Tables link not visible.")
            self.assertTrue(any(link.text == "Chairs" for link in nav_links), "Chairs link not visible.")

            # Check for cookie consent button
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookie_button.is_displayed(), "Cookie consent button not visible.")

            # Account and cart icons
            account_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "account-setting-active")))
            self.assertTrue(account_button.is_displayed(), "Account icon not visible.")

            cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))
            self.assertTrue(cart_button.is_displayed(), "Cart icon not visible.")

            # Login/Register tabs
            login_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='login']")))
            self.assertTrue(login_tab.is_displayed(), "Login tab not visible.")

            register_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='register']")))
            self.assertTrue(register_tab.is_displayed(), "Register tab not visible.")

            # Login Form elements
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            self.assertTrue(email_input.is_displayed(), "Email input not visible in login form.")

            password_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "user-password")))
            self.assertTrue(password_input.is_displayed(), "Password input not visible in login form.")

            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//form//button/span[text()='Login']")))
            self.assertTrue(login_button.is_displayed(), "Login button not visible in login form.")

        except Exception as e:
            self.fail(f"UI element verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()