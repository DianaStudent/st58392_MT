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

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        try:
            # Check header
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
            
            # Verify main menu links
            self.assertTrue(self.driver.find_element(By.XPATH, "//a[text()='Home']").is_displayed())
            self.assertTrue(self.driver.find_element(By.XPATH, "//a[text()='Tables']").is_displayed())
            self.assertTrue(self.driver.find_element(By.XPATH, "//a[text()='Chairs']").is_displayed())

            # Check login forms and buttons
            self.assertTrue(self.driver.find_element(By.NAME, 'email').is_displayed())
            self.assertTrue(self.driver.find_element(By.NAME, 'password').is_displayed())
            self.assertTrue(self.driver.find_element(By.NAME, 'repeatPassword').is_displayed())
            self.assertTrue(self.driver.find_element(By.NAME, 'firstName').is_displayed())
            self.assertTrue(self.driver.find_element(By.NAME, 'lastName').is_displayed())
            self.assertTrue(self.driver.find_element(By.XPATH, "//button/span[text()='Register']").is_displayed())

            # Interact with "Register" button
            register_button = self.driver.find_element(By.XPATH, "//button/span[text()='Register']")
            self.assertTrue(register_button.is_enabled())  # Ensure button is enabled
            register_button.click()

            # Check footer
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
            self.assertTrue(footer.is_displayed())

        except Exception as e:
            self.fail(f'UI element missing or not visible: {str(e)}')


if __name__ == "__main__":
    unittest.main()