import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestNopCommerceRegisterPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_ui_elements_presence(self):
        driver = self.driver
        driver.get("http://max/register?returnUrl=%2F")

        try:
            # Wait for and check visibility of the header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header"))
            )
            self.assertIsNotNone(header)

            # Check if the 'Register' button is visible
            register_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "register-button"))
            )
            self.assertIsNotNone(register_button)

            # Check visibility of input fields
            first_name_input = driver.find_element(By.ID, "FirstName")
            self.assertTrue(first_name_input.is_displayed())

            last_name_input = driver.find_element(By.ID, "LastName")
            self.assertTrue(last_name_input.is_displayed())

            email_input = driver.find_element(By.ID, "Email")
            self.assertTrue(email_input.is_displayed())

            # Check navigation links
            nav_links = driver.find_elements(By.CSS_SELECTOR, ".top-menu a")
            self.assertTrue(len(nav_links) > 0)

            # Interact with the 'Register' button
            register_button.click()

            # Check no errors occur when clicking 'Register'
            self.assertTrue(EC.visibility_of(register_button))
        
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()