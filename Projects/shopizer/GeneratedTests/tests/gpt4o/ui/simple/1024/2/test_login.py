import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo a img")))
            self.assertTrue(logo.is_displayed(), "Logo is not visible.")
        except:
            self.fail("Logo element is missing or not visible")

        # Check navigation menu
        try:
            nav_home = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertTrue(nav_home.is_displayed(), "Home link is not visible.")

            nav_tables = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.assertTrue(nav_tables.is_displayed(), "Tables link is not visible.")

            nav_chairs = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            self.assertTrue(nav_chairs.is_displayed(), "Chairs link is not visible.")
        except:
            self.fail("Navigation menu elements are missing or not visible")

        # Check login/register links
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            self.assertTrue(login_link.is_displayed(), "Login link is not visible.")

            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(register_link.is_displayed(), "Register link is not visible.")
        except:
            self.fail("Login/Register links are missing or not visible")

        # Check login form elements
        driver.get("http://localhost/login")
        try:
            username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            self.assertTrue(username_input.is_displayed(), "Username field is not visible.")

            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            self.assertTrue(password_input.is_displayed(), "Password field is not visible.")

            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
            self.assertTrue(login_button.is_displayed(), "Login button is not visible.")
        except:
            self.fail("Login form elements are missing or not visible")

        # Check cookie consent button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookie_button.is_displayed(), "Cookie consent button is not visible.")
        except:
            self.fail("Cookie consent button is missing or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)