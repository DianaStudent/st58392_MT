import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check for navigation links
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))

        # Check for login form fields
        self.wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
        self.wait.until(EC.visibility_of_element_located((By.NAME, 'loginPassword')))

        # Check for buttons
        self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))

        # Check for registration link
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))

        # Interact with elements
        accept_button = driver.find_element(By.ID, 'rcc-confirm-button')
        accept_button.click()

        login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
        login_button.click()
        
        # Check that URL is correctly updated or any visible change
        current_url = driver.current_url
        self.assertEqual(current_url, "http://localhost/login")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()