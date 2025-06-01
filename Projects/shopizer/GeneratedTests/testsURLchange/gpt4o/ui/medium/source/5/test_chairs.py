import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check presence of key interface elements
        try:
            # Header link - Home
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Home']")))
            self.assertTrue(home_link.is_displayed(), "Home link not visible")

            # Header link - Tables
            tables_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Tables']")))
            self.assertTrue(tables_link.is_displayed(), "Tables link not visible")

            # Header link - Chairs
            chairs_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Chairs']")))
            self.assertTrue(chairs_link.is_displayed(), "Chairs link not visible")

            # Footer - Subscribe form
            email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
            self.assertTrue(email_input.is_displayed(), "Email input not visible")

            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button")))
            self.assertTrue(subscribe_button.is_displayed(), "Subscribe button not visible")

            # Cookie consent button
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookie_button.is_displayed(), "Cookie consent button not visible")

        except Exception as e:
            self.fail(f"UI element verification failed: {str(e)}")

        # Interact with an element
        try:
            # Click on 'Tables' link and verify the page
            tables_link.click()
            wait.until(EC.url_contains("/category/tables"))
            current_url = driver.current_url
            self.assertIn("/category/tables", current_url, "Tables page did not load correctly")

            # Click cookie consent button
            cookie_button.click()
        except Exception as e:
            self.fail(f"Interaction failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()