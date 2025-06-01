import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.driver.maximize_window()

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header links
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-register")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-login")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-wishlist")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-cart")))
        except Exception as e:
            self.fail(f"Header link elements are not visible: {e}")

        # Check search box
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            self.assertTrue(search_box.is_displayed() and search_button.is_displayed())
        except Exception as e:
            self.fail(f"Search box elements are not visible: {e}")

        # Check registration form fields
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "gender-male")))
            wait.until(EC.visibility_of_element_located((By.ID, "gender-female")))
            wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Company")))
            wait.until(EC.visibility_of_element_located((By.ID, "Newsletter")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
            wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        except Exception as e:
            self.fail(f"Registration form fields are not visible: {e}")

        # Check footer links
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sitemap")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Privacy notice")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Conditions of Use")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Follow us")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Subscribe")))
        except Exception as e:
            self.fail(f"Footer link elements are not visible: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()