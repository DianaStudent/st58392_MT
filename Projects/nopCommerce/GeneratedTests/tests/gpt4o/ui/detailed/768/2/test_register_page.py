import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestWebPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check visibility of header
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        except Exception:
            self.fail("Header is not visible on the page.")

        # Check visibility of footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        except Exception:
            self.fail("Footer is not visible on the page.")

        # Verify presence of Register button
        try:
            register_button = wait.until(EC.visibility_of_element_located((By.ID, 'register-button')))
            register_button.click()  # Interact with the button
        except Exception:
            self.fail("Register button is not visible on the page.")

        # Check visibility of gender radio buttons
        try:
            gender_male = wait.until(EC.visibility_of_element_located((By.ID, 'gender-male')))
            gender_female = wait.until(EC.visibility_of_element_located((By.ID, 'gender-female')))
        except Exception:
            self.fail("Gender radio buttons are not visible on the page.")

        # Check visibility of First Name, Last Name, Email fields
        for field_id in ['FirstName', 'LastName', 'Email']:
            try:
                field = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            except Exception:
                self.fail(f"{field_id} field is not visible on the page.")

        # Check visibility of Password and Confirm Password fields
        for field_id in ['Password', 'ConfirmPassword']:
            try:
                wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            except Exception:
                self.fail(f"{field_id} field is not visible on the page.")

        # Verify presence of links in header menu
        header_links = ['/', '/newproducts', '/search', '/customer/info', '/blog', '/contactus']
        for link in header_links:
            try:
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"a[href='{link}']")))
            except Exception:
                self.fail(f"Link with href {link} is not visible in the header menu.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()