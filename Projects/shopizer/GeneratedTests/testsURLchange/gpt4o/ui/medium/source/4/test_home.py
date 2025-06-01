import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Failed to find one or more navigation links.")

        # Verify buttons and inputs
        try:
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            subscribe_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Subscribe']")))
        except:
            self.fail("Failed to find one or more buttons or inputs.")

        # Verify banner images
        try:
            banner_image = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='banner']")))
            promo_image = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='promo20']")))
        except:
            self.fail("Failed to find one or more banner images.")

        # Interact with elements
        try:
            accept_cookies_button.click()
            subscribe_input.send_keys("test@example.com")
            subscribe_button.click()
        except:
            self.fail("Failed to interact with elements.")

        # Verify no errors occurred
        self.assertEqual(driver.title, "Default store")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()