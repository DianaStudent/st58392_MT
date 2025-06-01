import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.set_window_size(1920, 1080)

    def tearDown(self):
        self.driver.quit()

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        if not header:
            self.fail("Header not found")

        # Check the home link
        home_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/']")))
        if not home_link:
            self.fail("Home link not found")

        # Check the tables link
        tables_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/category/tables']")))
        if not tables_link:
            self.fail("Tables link not found")

        # Check the chairs link
        chairs_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/category/chairs']")))
        if not chairs_link:
            self.fail("Chairs link not found")

        # Check the login link
        login_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/login']")))
        if not login_link:
            self.fail("Login link not found")

        # Check the register link
        register_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/register']")))
        if not register_link:
            self.fail("Register link not found")

        # Check login form elements
        login_link.click()
        username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        password_field = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "user-password")))
        remember_me_checkbox = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='checkbox']")))
        login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))

        if not (username_field and password_field and remember_me_checkbox and login_button):
            self.fail("One or more login form elements not found or visible")

        # Check register form elements
        register_link.click()
        email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        new_password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        repeat_password_field = wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
        first_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        last_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
        country_select = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "select")))
        register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']")))

        if not (email_field and new_password_field and repeat_password_field and first_name_field and last_name_field and country_select and register_button):
            self.fail("One or more register form elements not found or visible")

        # Check footer elements
        footer_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-logo a img")))
        subscribe_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form .email")))
        subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form .button")))

        if not (footer_logo and subscribe_field and subscribe_button):
            self.fail("One or more footer elements not found or visible")


if __name__ == "__main__":
    unittest.main()