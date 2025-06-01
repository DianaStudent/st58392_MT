import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopizerUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        except:
            self.fail("Header is not visible")

        # Verify navigation links
        nav_links = ['Home', 'Tables', 'Chairs']
        for link_text in nav_links:
            try:
                nav_link = self.wait.until(EC.visibility_of_element_located(
                    (By.LINK_TEXT, link_text)))
            except:
                self.fail(f"Navigation link '{link_text}' is missing or not visible")

        # Verify login form elements
        try:
            username = self.wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
            password = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'user-password')))
            login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        except:
            self.fail("Login form elements are missing or not visible")

        # Verify Cookie Consent Button
        try:
            cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        except:
            self.fail("Cookie consent button is missing or not visible")

        # Verify footer elements
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
        except:
            self.fail("Footer is not visible")

        # Interact with the login button
        try:
            login_button.click()
        except:
            self.fail("Unable to click the login button")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()