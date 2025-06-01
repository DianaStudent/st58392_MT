import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check if logo is present
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo a img")))
        except:
            self.fail("Logo is not visible")

        # Check if navigation links are present
        nav_links = {
            "Home": "/",
            "Tables": "/category/tables",
            "Chairs": "/category/chairs",
            "Login": "/login",
            "Register": "/register"
        }
        
        for link_text, link_href in nav_links.items():
            try:
                nav_link = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link_href}']")))
            except:
                self.fail(f"Navigation link {link_text} is not visible")

        # Check login form fields and buttons
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']/span[text()='Login']")))
        except:
            self.fail("Login form fields or button are not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()