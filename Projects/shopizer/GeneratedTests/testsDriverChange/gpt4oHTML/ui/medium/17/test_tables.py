import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_and_interactions(self):
        driver = self.driver

        # Step 1: Check for key interface elements
        try:
            # Check for navigation links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            
            # Check for buttons, inputs and banners
            self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        except:
            self.fail("A required UI element is missing or not visible.")

        # Step 2: Interact with "Accept cookies" button
        try:
            accept_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            accept_button.click()

            # Verify that the button no longer appears on the page (assuming it disappears after clicking)
            self.assertIsNone(driver.find_elements(By.ID, "rcc-confirm-button"))
        except:
            self.fail("UI did not update as expected after interacting with an element.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()