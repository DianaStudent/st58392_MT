import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for header elements
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-area")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Home']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Tables']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Chairs']")))
        except Exception as e:
            self.fail(f"Header elements not found: {str(e)}")

        # Check for button presence
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except Exception as e:
            self.fail(f"Cookie confirm button not found: {str(e)}")

        # Interact with the button
        try:
            cookie_button.click()
            # Verify the UI reacts to button click, e.g., button disappears after clicking
            wait.until(EC.invisibility_of_element_located((By.ID, "rcc-confirm-button")))
        except Exception as e:
            self.fail(f"Button interaction failed: {str(e)}")

        # Check footer elements
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-area")))
        except Exception as e:
            self.fail(f"Footer elements not visible: {str(e)}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()