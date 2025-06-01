import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode for faster execution and to avoid opening a browser window
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        try:
            # Click on "Sign in"
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()

            # Wait for login form to load
            login_email = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )

            # Enter email
            login_email.send_keys("test@user.com")

            # Enter password
            login_password = driver.find_element(By.ID, "field-password")
            login_password.send_keys("test@user1")

            # Click on 'Sign in' button
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "submit-login"))
            )
            sign_in_button.click()

            # Verify sign out is visible after login
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            
            # Assert that Sign out link is present, indicating successful login
            self.assertTrue(sign_out_link.is_displayed())

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")

if __name__ == "__main__":
    unittest.main()