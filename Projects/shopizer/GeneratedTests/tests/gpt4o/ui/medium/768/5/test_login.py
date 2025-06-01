from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestShopizerUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/login')
    
    def test_ui_elements_and_interactions(self):
        driver = self.driver

        # Wait for and check presence of header
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "header-area"))
        )
        self.assertIsNotNone(header, "Header is not present or visible")

        # Check main navigation links
        for link_text in ['Home', 'Tables', 'Chairs']:
            link_xpath = f"//a[text()='{link_text}']"
            nav_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, link_xpath))
            )
            self.assertIsNotNone(nav_link, f"{link_text} link is not present or visible")

        # Check login form fields
        username_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        self.assertIsNotNone(username_input, "Username input is not present or visible")

        password_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "loginPassword"))
        )
        self.assertIsNotNone(password_input, "Password input is not present or visible")

        # Check login button and interact with it
        login_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']"))
        )
        self.assertIsNotNone(login_button, "Login button is not present or visible")
        
        # Trying to click login button
        login_button.click()

        # Checking the presence of some element after login button click to confirm no UI errors
        # This can be customized based on behavior

        # Example confirmation by checking some visual change
        try:
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//p[@class='header-contact-info']"))
            )
        except:
            self.fail("UI did not update as expected after clicking login")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()