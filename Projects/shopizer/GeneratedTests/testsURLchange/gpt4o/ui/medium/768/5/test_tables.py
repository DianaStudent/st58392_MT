import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver with Chrome
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://localhost/")

        try:
            # Wait for and check the presence of navigation links
            nav_links = [
                ('Home', '/'),
                ('Tables', '/category/tables'),
                ('Chairs', '/category/chairs')
            ]
            for name, partial_href in nav_links:
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, f"//a[contains(@href, '{partial_href}')]"))
                )
            
            # Wait for and check key buttons' presence and visibility
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'rcc-confirm-button'))
            )
            
            # Interact with the "Accept Cookies" button
            accept_cookies_button = driver.find_element(By.ID, "rcc-confirm-button")
            accept_cookies_button.click()
            
            # Verify header is visible
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'header-area'))
            )

            # Verify presence of Footer elements
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area'))
            )

        except Exception as e:
            self.fail(f"Test failed due to an exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()