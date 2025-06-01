import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    
    def setUp(self):
        # Set up the web driver using ChromeDriverManager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)  # Implicit wait of 10 seconds
        self.driver.maximize_window()
        self.base_url = "http://localhost/"
    
    def test_ui_elements(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # Define a WebDriverWait for later use
        wait = WebDriverWait(driver, 20)
        
        # Check navigation links
        nav_links = {
            "Home": "/",
            "Tables": "/category/tables",
            "Chairs": "/category/chairs"
        }
        
        for link_text, link_url in nav_links.items():
            try:
                link = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[text()='{link_text}']")))
                self.assertTrue(link.is_displayed())
                self.assertEqual(link.get_attribute('href'), self.base_url + link_url.lstrip('/'))
            except Exception as e:
                self.fail(f"Navigation link for {link_text} is missing or incorrect: {str(e)}")
        
        # Check header and button presence on the page
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-area")))
            self.assertTrue(header.is_displayed(), "Header is missing or not visible.")
        except Exception as e:
            self.fail(f"Header check failed: {str(e)}")
        
        # Interact with "Accept cookies" button
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
            # Add any additional checks to ensure UI updates if necessary
        except Exception as e:
            self.fail(f"Interaction with 'Accept cookies' button failed: {str(e)}")
        
        # Check presence of login/register buttons
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(login_link.is_displayed(), "Login link is missing or not visible.")
            self.assertTrue(register_link.is_displayed(), "Register link is missing or not visible.")
        except Exception as e:
            self.fail(f"Login/Register buttons check failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()