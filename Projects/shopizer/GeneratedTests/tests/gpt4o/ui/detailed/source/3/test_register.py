import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver

        # Wait for and check header
        try:
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header-area"))
            )
        except:
            self.fail("Header is not visible.")

        # Wait for and check main navigation links
        try:
            home_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
            )
            tables_link = driver.find_element(By.LINK_TEXT, "Tables")
            chairs_link = driver.find_element(By.LINK_TEXT, "Chairs")
        except:
            self.fail("Main navigation links are missing or not visible.")

        # Wait for and check footer
        try:
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "footer-area"))
            )
        except:
            self.fail("Footer is not visible.")

        # Wait for and check login link
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
            )
        except:
            self.fail("Login link is not visible.")

        # Check presence of Login and Register forms
        driver.get("http://localhost/login")
        try:
            email_field_login = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            password_field_login = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
        except:
            self.fail("Login form elements are missing or not visible.")

        driver.get("http://localhost/register")
        try:
            email_field_register = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "email"))
            )
            password_field_register = driver.find_element(By.NAME, "password")
            repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
            first_name_field = driver.find_element(By.NAME, "firstName")
            last_name_field = driver.find_element(By.NAME, "lastName")
            register_button = driver.find_element(By.XPATH, "//button/span[text()='Register']")
        except:
            self.fail("Register form elements are missing or not visible.")

        # Interact with UI elements - Click on navigation links
        home_link.click()
        WebDriverWait(driver, 20).until(
            EC.url_to_be("http://localhost/")
        )
        tables_link.click()
        WebDriverWait(driver, 20).until(
            EC.url_to_be("http://localhost/category/tables")
        )

        # Interact - Accept Cookies
        try:
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Accept Cookies button is not visible or not clickable.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()