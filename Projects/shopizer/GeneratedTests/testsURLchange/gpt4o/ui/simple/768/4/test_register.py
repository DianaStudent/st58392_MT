import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check presence of main header/logo
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "logo"))
            )

            # Check presence of navbar links
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Tables"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Chairs"))
            )

            # Check presence of login/register form on login page
            driver.get("http://localhost/login")
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "loginPassword"))
            )

            # Check presence of register form fields
            driver.get("http://localhost/register")
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "email"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "password"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "repeatPassword"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "firstName"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "lastName"))
            )

            # Check presence of footer subscribe button
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "button"))
            )

        except Exception as e:
            self.fail(f"UI element check failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()