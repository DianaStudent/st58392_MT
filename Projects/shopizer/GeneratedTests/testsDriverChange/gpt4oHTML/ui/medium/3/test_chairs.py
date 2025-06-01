import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def tearDown(self):
        # Quit the driver after the test
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the presence of the navigation links
        try:
            nav_links = ['Home', 'Tables', 'Chairs']
            for link_text in nav_links:
                nav_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertTrue(nav_link.is_displayed())
        except Exception as e:
            self.fail(f"Navigation link missing or not visible: {str(e)}")

        # Check the presence of key buttons and elements
        try:
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Login')))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
            
            # Assert visibility
            self.assertTrue(accept_cookies_button.is_displayed())
            self.assertTrue(login_link.is_displayed())
            self.assertTrue(register_link.is_displayed())
            
            # Interaction
            accept_cookies_button.click()
            
            # Verify the button no longer exists after clicking (this could be part of any UI update verification)
            with self.assertRaises(Exception):
                wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))

        except Exception as e:
            self.fail(f"UI element interaction caused an unexpected problem: {str(e)}")

if __name__ == "__main__":
    unittest.main()