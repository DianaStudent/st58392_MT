import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestPageElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://max/register?returnUrl=%2F")
        
        # Verify the presence of key UI elements
        elements_to_check = {
            "Register Header": (By.XPATH, "//h1[text()='Register']"),
            "First Name Input": (By.ID, "FirstName"),
            "Last Name Input": (By.ID, "LastName"),
            "Email Input": (By.ID, "Email"),
            "Password Input": (By.ID, "Password"),
            "Confirm Password Input": (By.ID, "ConfirmPassword"),
            "Register Button": (By.ID, "register-button")
        }
        
        for elem_name, locator in elements_to_check.items():
            try:
                element = self.wait.until(EC.visibility_of_element_located(locator))
                self.assertTrue(element.is_displayed(), f"{elem_name} is not visible.")
            except Exception as e:
                self.fail(f"{elem_name} is not found or not visible: {str(e)}")
        
        # Interact with an element (e.g., click Register button)
        register_button = driver.find_element(By.ID, "register-button")
        ActionChains(driver).move_to_element(register_button).click().perform()
        
        # Verify no error after interaction
        notifications_error = driver.find_element(By.ID, "dialog-notifications-error")
        self.assertFalse(notifications_error.is_displayed(), "Error notification is visible after registration attempt.")
        
        # Verify the user stays on the registration page
        self.assertIn("register", driver.current_url, "Redirected from register page after clicking register without filling data.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()