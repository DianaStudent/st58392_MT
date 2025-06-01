import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterPageUI(unittest.TestCase):

    def setUp(self):
        # Set up ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the registration page
        driver.get("http://max/register?returnUrl=%2F")

        # Check for presence of navigation links
        nav_links = [
            "/register?returnUrl=%2F", 
            "/login?returnUrl=%2F", 
            "/wishlist", 
            "/cart",
            "/", 
            "/newproducts", 
            "/search", 
            "/customer/info", 
            "/blog", 
            "/contactus"
        ]
        for link in nav_links:
            element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"a[href='{link}']")))
            if not element.is_displayed():
                self.fail(f"Navigation link {link} is not visible")

        # Check for presence of form fields
        fields = ["FirstName", "LastName", "Email", "Company", "Password", "ConfirmPassword"]
        for field_id in fields:
            element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            if not element.is_displayed():
                self.fail(f"Input field with id {field_id} is not visible")

        # Check for presence of register button
        register_button = wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        if not register_button.is_displayed():
            self.fail("Register button is not visible")

        # Interact with Register button
        register_button.click()

        # Verify that the form interaction has no errors visually
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "field-validation-valid")))
        except:
            self.fail("UI did not update as expected after clicking register")

    def tearDown(self):
        # Close the driver
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()