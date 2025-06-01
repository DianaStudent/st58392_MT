import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header presence
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header is not visible.")

        # Check navigation links
        nav_links = ["Home", "Tables", "Chairs"]
        for link_text in nav_links:
            try:
                nav_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except:
                self.fail(f"Navigation link '{link_text}' is not visible.")

        # Check login link
        try:
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            login_link.click()
        except:
            self.fail("Login link is not clickable or not visible.")

        # Check form fields and button on the login page
        try:
            email_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        except:
            self.fail("Login form elements are missing.")

        # Check footer presence
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()