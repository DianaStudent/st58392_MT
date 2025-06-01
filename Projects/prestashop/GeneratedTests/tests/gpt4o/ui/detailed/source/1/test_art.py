import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        # Check header, footer, navigation
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            navigation = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))
        except:
            self.fail("Structural elements like header, footer, or navigation are missing.")

        # Check presence and visibility of input fields, buttons, labels, and sections
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.NAME, "submitNewsletter")))
            signin_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account")))
            language_selector = self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_language_selector")))
        except:
            self.fail("Some UI elements like input fields, buttons, or links are missing.")

        # Interact with key UI elements
        try:
            signin_link.click()
            self.wait.until(EC.url_contains("http://localhost:8080/en/login"))
            self.driver.back()
            register_link.click()
            self.wait.until(EC.url_contains("http://localhost:8080/en/registration"))
            self.driver.back()
        except:
            self.fail("Interaction with UI elements like buttons failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()