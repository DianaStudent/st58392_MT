import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence(self):
        driver = self.driver

        # Wait for and check the presence of key UI elements
        try:
            # Header links
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Login/Register form
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "username")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))

            # Click 'Login' and verify no errors
            login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
            login_button.click()

            # Verify UI does not have errors (by checking some visual still exist)
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

if __name__ == "__main__":
    unittest.main()