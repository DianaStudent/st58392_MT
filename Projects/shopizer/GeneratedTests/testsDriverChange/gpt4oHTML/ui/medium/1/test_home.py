import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence_and_interaction(self):
        driver = self.driver
        
        # Confirm the presence of key interface elements
        try:
            # Navigation links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Check Cookie consent button
            cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            
            # Check buttons, inputs and other UI components
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.icon-cart")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.email")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button")))

            # Banners or promo images
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='banner']")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='promo20']")))

        except Exception as e:
            self.fail(f"UI element missing or not visible: {e}")

        # Interact with elements - Click on accept cookies button and verify it no longer appears
        try:
            cookie_button.click()
            self.wait.until(EC.invisibility_of_element_located((By.ID, "rcc-confirm-button")))

        except Exception as e:
            self.fail(f"UI interaction failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()