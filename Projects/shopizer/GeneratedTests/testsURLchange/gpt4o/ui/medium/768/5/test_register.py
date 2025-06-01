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
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertTrue(home_link.is_displayed())

            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.assertTrue(tables_link.is_displayed())

            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            self.assertTrue(chairs_link.is_displayed())
        except Exception as e:
            self.fail(f"Navigation link not found or not visible: {e}")
        
        # Check Login/Register tabs
        try:
            login_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@role='tab'][contains(text(), 'Login')]")))
            self.assertTrue(login_tab.is_displayed())

            register_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@role='tab'][contains(text(), 'Register')]")))
            self.assertTrue(register_tab.is_displayed())
        except Exception as e:
            self.fail(f"Login/Register tabs not found or not visible: {e}")

        # Check form fields and button
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            self.assertTrue(email_input.is_displayed())

            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            self.assertTrue(password_input.is_displayed())

            register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']")))
            self.assertTrue(register_button.is_displayed())
        except Exception as e:
            self.fail(f"Form fields or button not found or not visible: {e}")

        # Interact with 'Register' tab
        try:
            register_tab.click()
            register_form = wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Register']")))
            self.assertTrue(register_form.is_displayed())
        except Exception as e:
            self.fail(f"Unable to interact with 'Register' tab: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()