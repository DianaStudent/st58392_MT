import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver using ChromeDriverManager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check that the header and navigation are present
        try:
            header = wait.until(EC.visibility_of_element_located((By.XPATH, "//header[@class='header-area clearfix']")))
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//nav//a")))
        except Exception as e:
            self.fail(f"Exception during finding header/nav links: {e}")

        # Check navigation links
        expected_links = ['/', '/category/tables', '/category/chairs']
        actual_links = [link.get_attribute('href') for link in nav_links]
        for expected_link in expected_links:
            self.assertIn(expected_link, actual_links, f"Missing expected navigation link: {expected_link}")

        # Check presence of key interface elements
        try:
            cookie_banner = wait.until(EC.visibility_of_element_located((
                By.XPATH, "//div[@class='CookieConsent']")))
            login_button = wait.until(EC.visibility_of_element_located((
                By.XPATH, "//a[@href='/login']")))
        except Exception as e:
            self.fail(f"Exception during finding key interface elements: {e}")

        # Interact with the 'Accept Cookies' button
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Failed to click 'Accept Cookies' button: {e}")

        # Verify UI updates - Check the cookie consent is not displayed anymore
        try:
            wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='CookieConsent']")))
        except Exception as e:
            self.fail(f"Failed to verify that the cookie banner is hidden: {e}")

    def tearDown(self):
        # Clean up and close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()