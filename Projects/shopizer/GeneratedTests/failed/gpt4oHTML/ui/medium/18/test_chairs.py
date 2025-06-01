from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check presence of header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'header-area'))
            )
            
            # Check presence of 'Home' navigation link
            home_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, 'Home'))
            )

            # Check presence of 'Tables' navigation link
            tables_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, 'Tables'))
            )

            # Check presence of 'Chairs' navigation link
            chairs_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs'))
            )

            # Check presence of 'Login' link
            login_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.account-dropdown a[href="/login"]'))
            )

            # Check presence of 'Register' link
            register_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.account-dropdown a[href="/register"]'))
            )

            # Check presence of Cookie Consent Banner
            cookie_banner = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'CookieConsent'))
            )

            # Interacting with "Accept cookies" button
            accept_button = cookie_banner.find_element(By.ID, 'rcc-confirm-button')
            accept_button.click()
            
            # Check that interaction does not cause any errors
            WebDriverWait(driver, 20).until(
                EC.invisibility_of_element((By.CLASS_NAME, 'CookieConsent'))
            )

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()