import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class UITestSuite(unittest.TestCase):
    def setUp(self):
        # Install and set up the ChromeDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('http://localhost/')

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Confirm the presence of main navigation links
        try:
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Home')))
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Tables')))
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Chairs')))
        except:
            self.fail("One or more main navigation links are missing.")

        # 2. Confirm the presence of login elements
        try:
            wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
            wait.until(EC.visibility_of_element_located((By.NAME, 'loginPassword')))
            wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]/span[text()="Login"]')))
        except:
            self.fail("One or more login elements are missing.")

        # 3. Interact with the "Accept cookies" button
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            cookie_button.click()
            # Check UI update here, if necessary
        except:
            self.fail("Cookie consent button interaction failed.")

        # 4. Check that the account setting button exists and is visible
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.account-setting-active')))
        except:
            self.fail("Account setting button is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()