from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UIComponentTest(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver using WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_ui_elements(self):
        driver = self.driver

        # 1. Open the page and verify presence of main UI components
        try:
            # Verify header and navigation links
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header.header-area')))
            self.assertIsNotNone(header, "Header is not present")

            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            self.assertIsNotNone(home_link, "Home link is not present")

            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
            self.assertIsNotNone(tables_link, "Tables link is not present")

            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
            self.assertIsNotNone(chairs_link, "Chairs link is not present")

            # Verify Accept button for cookies
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
            self.assertIsNotNone(accept_cookies_button, "Accept cookies button is not present")
            
            # Verify presence of input field for email subscription
            email_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.email')))
            self.assertIsNotNone(email_input, "Email input is not present")

            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.button')))
            self.assertIsNotNone(subscribe_button, "Subscribe button is not present")

            # Verify banner image
            banner_image = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.site-blocks-cover img')))
            self.assertIsNotNone(banner_image, "Banner image is not present")
            
            # 2. Interact with one element
            accept_cookies_button.click()
            
            # Verify button interaction by checking if the cookies consent div is hidden
            self.assertFalse(
                driver.find_element(By.CSS_SELECTOR, '.CookieConsent').is_displayed(),
                "Cookie consent message did not disappear after accepting"
            )

        except Exception as e:
            self.fail(f"Test failed due to {str(e)}")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()