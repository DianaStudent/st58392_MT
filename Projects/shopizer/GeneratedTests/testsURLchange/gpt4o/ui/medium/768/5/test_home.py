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

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/']")))
            tables_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/tables']")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/chairs']")))
            self.assertTrue(home_link.is_displayed(), "Home link is not visible.")
            self.assertTrue(tables_link.is_displayed(), "Tables link is not visible.")
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible.")
        except:
            self.fail("Navigation links are not present or visible.")

        # Check buttons
        try:
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
            self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible.")
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button is not present or visible.")

        # Check banners
        try:
            banner_image = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='banner']")))
            self.assertTrue(banner_image.is_displayed(), "Banner image is not visible.")
        except:
            self.fail("Banner image is not present or visible.")

        # Check form fields
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button")))
            self.assertTrue(email_input.is_displayed(), "Email input field is not visible.")
            self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible.")
        except:
            self.fail("Form elements are not present or visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()