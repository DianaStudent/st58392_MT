import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://max/register?returnUrl=%2F")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        # Verify header links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            new_products_link = driver.find_element(By.LINK_TEXT, "New products")
            search_link = driver.find_element(By.LINK_TEXT, "Search")
        except:
            self.fail("Header links are missing.")

        # Verify registration form fields
        try:
            first_name_field = driver.find_element(By.ID, "FirstName")
            last_name_field = driver.find_element(By.ID, "LastName")
            email_field = driver.find_element(By.ID, "Email")
            password_field = driver.find_element(By.ID, "Password")
            confirm_password_field = driver.find_element(By.ID, "ConfirmPassword")
            register_button = driver.find_element(By.ID, "register-button")
        except:
            self.fail("Registration form fields are missing.")

        # Verify search box
        try:
            search_box = driver.find_element(By.ID, "small-searchterms")
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        except:
            self.fail("Search box is missing.")

        # Interact with search box
        search_box.send_keys("Test")
        search_button.click()

        # Verify no errors appeared
        notification_error = driver.find_element(By.ID, "dialog-notifications-error")
        self.assertFalse(notification_error.is_displayed(), "Error notification should not be displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()