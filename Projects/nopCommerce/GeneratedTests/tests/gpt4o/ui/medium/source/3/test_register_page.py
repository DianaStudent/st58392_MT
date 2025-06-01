import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterPageUIElements(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://max/register?returnUrl=%2F")

        # Wait for the header elements and validate their presence
        header_links = [
            "/register?returnUrl=%2F", 
            "/login?returnUrl=%2F", 
            "/wishlist", 
            "/cart"
        ]

        for link in header_links:
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, f"a[href='{link}']"))
                )
                self.assertTrue(element.is_displayed(), f"Element with link {link} is not visible.")
            except:
                self.fail(f"Element with link {link} not found or not visible.")

        # Check for presence of form inputs
        form_element_ids = ["gender-male", "gender-female", "FirstName", "LastName", "Email", "Company", "Password", "ConfirmPassword"]
        for element_id in form_element_ids:
            try:
                input_element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.ID, element_id))
                )
                self.assertTrue(input_element.is_displayed(), f"Form input {element_id} is not visible.")
            except:
                self.fail(f"Form input {element_id} not found or not visible.")

        # Check presence of the Register button and interact with it
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "register-button"))
            )
            self.assertTrue(register_button.is_displayed(), "Register button is not visible.")
            register_button.click()

            self.assertNotIn("error", driver.page_source.lower(), "Errors found in the page source after clicking register.")
        except:
            self.fail("Register button not found or not clickable.")
        
    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()