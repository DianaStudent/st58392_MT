import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginScreen(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_login_screen_structure(self):
        # Check that structural elements (e.g., header, footer, navigation) are visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

        # Check the presence and visibility of input fields, buttons, labels, and sections
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "username"))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "password"))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "login-button"))))

    def test_login_button_click(self):
        # Interact with key UI elements (e.g., click buttons)
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()

        # Confirm that the UI reacts visually
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Login')]"))))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()