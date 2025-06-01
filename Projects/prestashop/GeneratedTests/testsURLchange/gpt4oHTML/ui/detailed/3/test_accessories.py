import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver
        
        # Use WebDriverWait for synchronization to wait until elements are present and visible
        wait = WebDriverWait(driver, 20)
        
        # 1. Check main UI components (header, footer, navigation)
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            main_navigation = wait.until(EC.visibility_of_element_located((By.ID, "_desktop_top_menu")))
        except:
            self.fail("One or more main UI components (header, footer, navigation) are missing or not visible.")
        
        # 2. Check presence and visibility of input fields, buttons, labels, and sections
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            language_selector = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "language-selector")))
            signin_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            cart_preview = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-preview")))
        except:
            self.fail("One or more expected elements (input fields, buttons, labels, or sections) are missing or not visible.")
        
        # 3. Interact with key UI elements (click buttons)
        try:
            signin_link.click()
            wait.until(EC.url_contains("login"))
        except:
            self.fail("Unable to click 'Sign in' link or it did not redirect to expected page.")
        
        # Navigate back to the home page for further checks
        driver.get("http://localhost:8080/en/")
        
        # Confirm UI reacts visually on button click like opening language dropdown
        try:
            language_selector_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-unstyle")))
            language_selector_button.click()
            dropdown_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "dropdown-menu")))
            self.assertTrue(dropdown_menu.is_displayed(), "Language dropdown did not open.")
        except:
            self.fail("Language selector did not behave as expected when interacted with.")
        
        # 4. Assert that no required UI element is missing
        # This is already covered in the above checks, any failure would raise a test failure
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()