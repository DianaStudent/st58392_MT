import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the presence of nav links
        home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))

        # Check the presence of the "Accept cookies" button
        accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))

        # Check the presence of the header
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))

        # Check that form fields are present on the Registration tab
        driver.get("http://localhost/register")
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        repeat_password_input = wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
        
        # Interact with an element - Click 'Accept cookies' button and check UI update
        accept_cookies_button.click()
        try:
            wait.until(EC.invisibility_of_element((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Failed to interact with 'Accept cookies' button or it did not update the UI as expected.")
        
        # Check interactive elements do not cause errors
        try:
            login_link.click()
            wait.until(EC.url_to_be("http://localhost/login"))
        except Exception as e:
            self.fail(f"Interaction with elements caused an error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()