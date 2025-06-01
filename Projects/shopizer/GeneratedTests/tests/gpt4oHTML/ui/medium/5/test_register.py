import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class TestUIProcess(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode for testing
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get('http://localhost/')

    def test_ui_elements_and_interaction(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Assert navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Assert login/register links
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))

            # Assert header
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))

            # Assert presence of cookie consent button and interact
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()

            # Assert that the button interaction did not cause any error in the UI
            consent_banner = driver.find_elements(By.CLASS_NAME, "CookieConsent")
            self.assertEqual(len(consent_banner), 0, "Cookie consent banner should be gone after accepting cookies.")

            # Assert presence of login/register form inputs
            login_email_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            login_password_input = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))

        except Exception as e:
            self.fail(f"UI element exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()