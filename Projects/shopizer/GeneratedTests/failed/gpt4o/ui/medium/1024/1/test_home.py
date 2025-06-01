from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_page_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            
            # Verify header elements
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[src*='logo']")))
            
            # Verify banner
            banner = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".site-blocks-cover img")))
            
            # Verify buttons
            accept_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            
            # Verify interaction with button
            accept_button.click()
            WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.CLASS_NAME, "CookieConsent")))
            
            # Verify inputs
            subscribe_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button")))

            # Click action and verification
            subscribe_button.click()
            # Placeholder where you'd verify result of the click, e.g., checking for toast message or similar

        except Exception as e:
            self.fail(f"Test failed due to missing element or unexpected error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()