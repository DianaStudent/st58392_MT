import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        # Set up the browser using WebDriver Manager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_UI_elements(self):
        driver = self.driver

        # Check header logo
        header_logo = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo a img"))
        )
        if not header_logo:
            self.fail("Header logo is not visible.")

        # Check navigation menu links
        home_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
        )
        tables_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Tables"))
        )
        chairs_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Chairs"))
        )

        if not (home_link and tables_link and chairs_link):
            self.fail("One or more navigation links are not visible.")

        # Check cookie consent button
        cookie_consent_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
        )
        if not cookie_consent_button:
            self.fail("Cookie consent button is not visible.")
        cookie_consent_button.click()

        # Navigate to login page and check elements
        login_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/login']"))
        )
        login_link.click()

        login_email = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        login_password = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "loginPassword"))
        )
        login_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
        )

        if not (login_email and login_password and login_button):
            self.fail("One or more login elements are not visible.")

        # Navigate to register page and check elements
        driver.get("http://localhost/register")

        register_email = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        register_password = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        register_repeat_password = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "repeatPassword"))
        )
        register_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
        )

        if not (register_email and register_password and register_repeat_password and register_button):
            self.fail("One or more register elements are not visible.")

    def tearDown(self):
        # Tear down the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()