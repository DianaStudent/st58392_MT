import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUISelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Confirm the presence of key interface elements
        try:
            # Confirm navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Confirm input fields
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))

            # Confirm buttons
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))

            # Confirm presence of a cookie consent button
            cookie_accept_btn = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))

        except Exception as e:
            self.fail(f"Essential UI elements are missing: {e}")

        # Interact with the elements
        try:
            # Click cookie consent button
            cookie_accept_btn.click()

            # Enter credentials
            email_input.send_keys("test@example.com")
            password_input.send_keys("password")

            # Click login button
            login_button.click()

            # Check no errors occur, you might check by verifying a successful login
            login_success_msg = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//p[@class='text-center' and text()='No items added to cart']")
            ))
            self.assertTrue(login_success_msg.is_displayed())

        except Exception as e:
            self.fail(f"Interacting with UI elements caused an error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()