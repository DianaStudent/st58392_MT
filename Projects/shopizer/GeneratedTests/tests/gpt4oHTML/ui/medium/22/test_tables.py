import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Confirm navigation links are present
        nav_links = {
            "Home": '/',
            "Tables": '/category/tables',
            "Chairs": '/category/chairs',
            "Login": '/login',
            "Register": '/register'
        }
        
        for name, href in nav_links.items():
            link = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{href}']")))
            self.assertTrue(link.is_displayed(), f"{name} link should be visible")

        # Confirm presence of key banner (cookie consent)
        try:
            cookie_banner = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "CookieConsent")))
            self.assertTrue(cookie_banner.is_displayed(), "Cookie consent banner should be visible")
        except:
            self.fail("Cookie consent banner not found")

        # Confirm presence of key buttons
        try:
            accept_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_button.is_displayed(), "Accept cookies button should be visible")
        except:
            self.fail("Accept cookies button not found")

        # Interact with an element and confirm UI change
        accept_button.click()

        # Check that the banner is no longer visible after clicking accept
        try:
            wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "CookieConsent")))
        except:
            self.fail("Cookie consent banner should not be visible after clicking accept")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()