import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check visibility of header
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        except:
            self.fail("Header is not visible")

        # Check visibility of footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        except:
            self.fail("Footer is not visible")

        # Check visibility of navigation links
        try:
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//nav/ul/li/a")))
            required_links = ["Home", "Tables", "Chairs"]
            visible_links = [link.text for link in nav_links]
            for link in required_links:
                if link not in visible_links:
                    self.fail(f"Navigation link '{link}' is missing")
        except:
            self.fail("Navigation links are not visible")

        # Check presence and visibility of input fields
        try:
            username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            remember_checkbox = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='checkbox']")))
        except:
            self.fail("One of the input fields is not visible")

        # Check presence and visibility of buttons
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span[text()='Login']]")))
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("One of the buttons is not visible")

        # Interact with elements
        try:
            accept_cookies_button.click()
            login_button.click()
        except:
            self.fail("Unable to interact with buttons")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()