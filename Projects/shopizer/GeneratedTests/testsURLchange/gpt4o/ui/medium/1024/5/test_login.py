import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check presence of navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = driver.find_element(By.LINK_TEXT, "Tables")
            chairs_link = driver.find_element(By.LINK_TEXT, "Chairs")
        except Exception as e:
            self.fail(f"Navigation links are not present or visible: {str(e)}")
        
        # Confirm login input fields are present
        try:
            email_input = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@name='username'][@placeholder='Email address']")))
            password_input = driver.find_element(By.XPATH, "//input[@class='user-password'][@name='loginPassword']")
        except Exception as e:
            self.fail(f"Login input fields are not present or visible: {str(e)}")

        # Check login button is present
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span='Login']")))
        except Exception as e:
            self.fail(f"Login button is not present or visible: {str(e)}")

        # Interact with "Accept" cookies button and check UI update
        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except Exception as e:
            self.fail(f"Cookie 'Accept' button interaction failed: {str(e)}")
        
        # Verify no errors in UI after interaction
        try:
            error_elements = driver.find_elements(By.CLASS_NAME, "error")
            self.assertEqual(len(error_elements), 0, "Errors present in the UI after interaction")
        except Exception as e:
            self.fail(f"Error checking failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()