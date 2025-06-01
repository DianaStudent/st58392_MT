import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header logo
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo a img")))
        except:
            self.fail("Header logo is not visible.")

        # Verify navigation links
        try:
            nav_links = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".main-menu nav ul")))
        except:
            self.fail("Navigation links are not visible.")

        # Verify login form
        try:
            login_tab = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-rb-event-key='login']")))
            self.assertTrue(login_tab.is_displayed(), "Login tab is not visible.")
            
            username_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_field = driver.find_element(By.NAME, "loginPassword")
            
            self.assertTrue(username_field.is_displayed(), "Username field is not visible.")
            self.assertTrue(password_field.is_displayed(), "Password field is not visible.")
        except:
            self.fail("Login form elements are missing or not visible.")

        # Verify login button
        try:
            login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-box button[type='submit']")))
        except:
            self.fail("Login button is not visible.")

        # Verify footer elements
        try:
            footer_logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-logo a img")))
        except:
            self.fail("Footer logo is not visible.")

        try:
            footer_links = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-list ul")))
        except:
            self.fail("Footer links are not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()