import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver.quit()
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check main menu items visibility
        nav_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "main-menu")))
        self.assertTrue(nav_menu.is_displayed(), "Navigation menu is not visible")
        
        home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        self.assertTrue(home_link.is_displayed(), "Home link is not visible")

        tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")

        chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")

        # Check login form elements
        login_tab = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[data-rb-event-key="login"]')))
        self.assertTrue(login_tab.is_displayed(), "Login tab is not visible")
        
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        self.assertTrue(email_input.is_displayed(), "Email input is not visible")
        
        password_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "user-password")))
        self.assertTrue(password_input.is_displayed(), "Password input is not visible")
        
        login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))
        self.assertTrue(login_button.is_displayed(), "Login button is not visible")
        
        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Interact with UI elements
        login_button.click()
        
        # Confirm the interaction caused a visual response
        alert = wait.until(EC.alert_is_present())
        self.assertIsNotNone(alert, "No alert present after login attempt")
        if alert:
            alert.accept()

        # Check if any other required UI element is missing
        elements_to_check = [header, nav_menu, footer, email_input, 
                             password_input, login_button, home_link, 
                             tables_link, chairs_link]
        missing_elements = [e for e in elements_to_check if not e]
        
        if missing_elements:
            self.fail(f"Missing required UI elements: {missing_elements}")

if __name__ == "__main__":
    unittest.main()