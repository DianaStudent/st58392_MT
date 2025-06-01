import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestKeyUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Verify the presence of navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Verify the presence and visibility of buttons
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))

            # Verify the presence of form inputs
            email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']")))

            # Verify presence of banner images
            banner_image = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='banner']")))

            # Interact with "Accept Cookies" button
            accept_cookies_button.click()

            # Verify no errors occurred
            # Simulate a UI interaction that should result in a visible change
            home_link.click()
            home_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))

            # Check a visible element after interaction
            self.assertIn("Imports from the world", home_title.text)

        except Exception as e:
            self.fail(f"Test failed due to missing element or exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()