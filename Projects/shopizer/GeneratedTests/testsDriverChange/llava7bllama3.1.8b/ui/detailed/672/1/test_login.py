import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopRocket(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        # Open the login page
        self.driver.get("http://localhost/login")

        # Check structural elements (header, footer, navigation)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//header")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//footer")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//nav")))

        # Check presence and visibility of input fields, buttons, labels, and sections
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "email")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "password")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot Password?")))

        # Interact with key UI elements (click buttons)
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        button.click()

        # Confirm that the UI reacts visually
        self.assertEqual(self.driver.title, "Login")

        # Assert that no required UI element is missing
        self.failUnless(EC.visibility_of_element_located((By.NAME, "email")).present)
        self.failUnless(EC.visibility_of_element_located((By.NAME, "password")).present)
        self.failUnless(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")).present)

if __name__ == "__main__":
    unittest.main()