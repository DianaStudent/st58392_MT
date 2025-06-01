from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check main UI components presence

        # Check header and navigation links
        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        except:
            self.fail("Header not visible")

        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Clothes')))
        except:
            self.fail("Clothes link not visible")

        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accessories')))
        except:
            self.fail("Accessories link not visible")

        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Art')))
        except:
            self.fail("Art link not visible")

        # Check Sign in link
        try:
            sign_in_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sign in')))
        except:
            self.fail("Sign in link not visible")

        # Check footer presence
        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        except:
            self.fail("Footer not visible")

        # Check newsletter subscription
        try:
            wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
        except:
            self.fail("Email input for newsletter not visible")

        # Click Sign in to ensure navigation works
        sign_in_link.click()
        wait.until(EC.url_to_be("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"))

        # Check Register link
        try:
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Create account')))
        except:
            self.fail("Register link not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()