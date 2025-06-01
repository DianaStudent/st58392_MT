import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://max/"

    def test_ui_elements(self):
        driver = self.driver

        # Step 1: Open the page.
        driver.get(self.base_url)

        # Step 2: Confirm the presence of key interface elements.
        try:
            # Check for navigation links
            register_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "ico-register"))
            )
            login_link = driver.find_element(By.CLASS_NAME, "ico-login")
            self.assertTrue(register_link.is_displayed() and login_link.is_displayed(),
                            "Register or login link is not visible.")

            # Check for search box and button
            search_box = driver.find_element(By.ID, "small-searchterms")
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            self.assertTrue(search_box.is_displayed() and search_button.is_displayed(),
                            "Search box or button is not visible.")

            # Check for footer links
            footer_links = driver.find_elements(By.CSS_SELECTOR, ".footer-block .list li a")
            self.assertTrue(all(link.is_displayed() for link in footer_links),
                            "Some footer links are not visible.")

        except Exception as e:
            self.fail(f"Failed to find expected UI elements. Exception: {str(e)}")

        # Step 3: Interact with one or two elements
        try:
            # Click on the register link
            register_link.click()

            # Verify that clicking register updates the UI by checking the presence of registration form
            registration_form = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "registration-page"))
            )
            self.assertTrue(registration_form.is_displayed(), "Registration page did not load properly.")

        except Exception as e:
            self.fail(f"Interaction with UI elements failed. Exception: {str(e)}")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()