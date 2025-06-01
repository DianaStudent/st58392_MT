import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check navigation links
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/']"))), "Home link is not visible")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/tables']"))), "Tables link is not visible")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/chairs']"))), "Chairs link is not visible")
        
        # Check header logo
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='http://localhost:8080/static/files/DEFAULT/LOGO/shopizer_resized_transparent.png']"))), "Logo is not visible")

        # Check banner (Cookie consent)
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".CookieConsent"))), "Cookie consent banner is not visible")
        
        # Interact with cookie consent button
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except Exception as e:
            self.fail(f"Could not interact with accept cookies button: {str(e)}")

        # Check if the UI updates accordingly (cookie consent banner is no longer visible)
        self.assertTrue(wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".CookieConsent"))), "Cookie consent banner did not disappear")
        
        # Go to Register page to check form inputs
        register_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']")))
        register_link.click()
        
        # Verify presence of inputs in registration form
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.NAME, "email"))), "Email input is not visible in register form")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.NAME, "password"))), "Password input is not visible in register form")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword"))), "Repeat Password input is not visible in register form")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))), "First Name input is not visible in register form")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.NAME, "lastName"))), "Last Name input is not visible in register form")
        
        # Verify submit button
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[contains(text(), 'Register')]"))), "Register button is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()