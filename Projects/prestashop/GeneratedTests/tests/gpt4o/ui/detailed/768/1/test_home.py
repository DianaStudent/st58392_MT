import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDemoSite(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements_present(self):
        driver = self.driver

        try:
            # Verify header is visible
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'header'))
            )

            # Verify footer is visible
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'footer'))
            )

            # Verify main navigation links
            nav_links = ['3-clothes', '6-accessories', '9-art']
            for link in nav_links:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, f"//a[contains(@href, '{link}')]"))
                )
                self.assertTrue(element.is_displayed(), f"{link} link not visible.")

            # Verify login and registration links
            login_reg_links = ['login', 'registration']
            for link in login_reg_links:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, f"//a[contains(@href, '{link}')]"))
                )
                self.assertTrue(element.is_displayed(), f"{link} link not visible.")

            # Verify search input field is visible
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@name='s']"))
            )
            self.assertTrue(search_input.is_displayed(), "Search input not visible.")

            # Interact: Click on the login link and check if login page loads
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
            )
            login_button.click()

            # Verify login form is present
            login_form = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'login-form'))
            )
            self.assertTrue(login_form.is_displayed(), "Login form not visible after clicking login.")

        except Exception as e:
            self.fail(f"UI Element missing or not visible: {e}")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()