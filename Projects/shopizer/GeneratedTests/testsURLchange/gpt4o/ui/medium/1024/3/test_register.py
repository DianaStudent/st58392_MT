import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver

        # Check navigation links
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

        # Check accept cookies button
        cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        cookies_button.click()

        # Check login and register links
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))

        # Check form fields on register page
        driver.get("http://localhost/register")
        self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        self.wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
        self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        self.wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))

        # Check register button
        register_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']")))
        self.assertTrue(register_button.is_displayed(), "Register button is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()