import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )

            # Check footer
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "footer"))
            )

            # Check navigation links
            home_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
            )
            tables_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Tables"))
            )
            chairs_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Chairs"))
            )

            # Check login form
            username_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']"))
            )

            # Check register tab
            register_tab = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='register']"))
            )

            # Interact with elements
            register_tab.click()
            
        except Exception as e:
            self.fail(f"UI element is missing: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()