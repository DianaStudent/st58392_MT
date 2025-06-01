import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.driver.maximize_window()

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header presence
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header is not visible")

        # Check footer presence
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer is not visible")

        # Verify Login/Register tab presence
        try:
            login_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[h4[text()=' Login']]")))
            register_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[h4[text()=' Register']]")))
        except:
            self.fail("Login/Register tabs are not visible")

        # Verify input fields presence
        input_field_selectors = [
            (By.NAME, "email"),
            (By.NAME, "password"),
            (By.NAME, "repeatPassword"),
            (By.NAME, "firstName"),
            (By.NAME, "lastName"),
            (By.NAME, "stateProvince")
        ]

        for selector in input_field_selectors:
            try:
                input_field = wait.until(EC.visibility_of_element_located(selector))
            except:
                self.fail(f"Input field {selector[1]} is not visible")

        # Verify buttons presence
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Register']]")))
        except:
            self.fail("Required button is not visible or clickable")

        # Interact with Accept Cookies button
        accept_cookies_button.click()

        # Confirm that the UI reacts visually (example check here)
        try:
            wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "CookieConsent")))
        except:
            self.fail("Cookie consent banner did not disappear after accepting")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()