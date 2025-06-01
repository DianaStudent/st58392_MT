import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check presence of main UI components
        try:
            # Header area
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
            navbar_links = ['Home', 'Tables', 'Chairs']
            for link_text in navbar_links:
                link = header.find_element(By.LINK_TEXT, link_text)
                self.assertTrue(link.is_displayed(), f"{link_text} link is not displayed in header")
            
            # Confirm "Accept" button for cookies is present
            cookie_accept_btn = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookie_accept_btn.is_displayed(), "Accept cookies button is not displayed")

            # Confirm "Login" and "Register" buttons are present
            account_menu_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "account-setting-active")))
            account_menu_button.click()  # Open account settings menu
            
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            
            self.assertTrue(login_link.is_displayed(), "Login link is not displayed")
            self.assertTrue(register_link.is_displayed(), "Register link is not displayed")

            # Interact with one element
            cookie_accept_btn.click()  # Accept cookies
            
            # Verify banner disappears after click
            try:
                wait.until(EC.invisibility_of_element(cookie_accept_btn))
            except:
                self.fail("Cookie consent banner did not disappear after accepting")

        except Exception as e:
            self.fail(f"Exception occurred in test_ui_elements: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()