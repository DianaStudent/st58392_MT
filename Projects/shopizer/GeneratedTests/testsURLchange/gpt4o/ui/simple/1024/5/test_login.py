import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Check header elements
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo a img")))

            # Check navigation menu
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Check account links
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/login']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/register']")))

            # Check footer elements
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-area")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-logo a img")))

            # Verify cookie consent
            wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))

            # Check login form components
            wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")

if __name__ == "__main__":
    unittest.main()