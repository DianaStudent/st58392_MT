import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check if navigation links are present
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Check if login tab and fields are present
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Login']")))
            wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))

            # Check if register tab and fields are present
            register_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Register']")))
            register_tab.click()

            wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
            wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']")))

            # Interacting with an element: Click 'Accept cookies' button
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
            
            # Verify the cookie consent is no longer visible
            self.assertFalse(driver.find_elements(By.ID, "rcc-confirm-button"))

        except Exception as e:
            self.fail(f"UI element check failed: {str(e)}")

if __name__ == "__main__":
    unittest.main()