import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITestCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def tearDown(self):
        self.driver.quit()
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check visibility of main UI components
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
            self.assertTrue(header.is_displayed() and footer.is_displayed())
        except:
            self.fail("Header or footer is missing")

        # Check visibility and presence of navigation links
        try:
            nav_links = ["Home", "Tables", "Chairs"]
            for link_text in nav_links:
                link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertTrue(link.is_displayed())
        except:
            self.fail(f"Navigation link {link_text} is missing")

        # Check presence and visibility of login/register tabs
        try:
            login_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='tab' and text()=' Login']")))
            register_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='tab' and text()=' Register']")))
            self.assertTrue(login_tab.is_displayed() and register_tab.is_displayed())
        except:
            self.fail("Login or Register tab is missing")

        # Check presence of input fields
        inputs = [
            (By.NAME, "username"),
            (By.NAME, "loginPassword"),
            (By.NAME, "email"),
            (By.NAME, "password"),
            (By.NAME, "repeatPassword"),
            (By.NAME, "firstName"),
            (By.NAME, "lastName"),
            (By.NAME, "stateProvince")
        ]
        for input_selector in inputs:
            try:
                input_field = wait.until(EC.visibility_of_element_located(input_selector))
                self.assertTrue(input_field.is_displayed())
            except:
                self.fail(f"Input field {input_selector} is missing or not visible")

        # Check buttons
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Register']")))
            self.assertTrue(accept_cookies_button.is_displayed() and register_button.is_displayed())
            
            # Interact with cookie button
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button or Register button is missing or not clickable")
        
        # Confirm no elements are missing
        self.assertTrue(True, "All required UI elements are present and visible")

if __name__ == "__main__":
    unittest.main()