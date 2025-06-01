import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopizerUITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_present(self):
        driver = self.driver
        wait = self.wait

        # Check logo is present
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo img")))
        except:
            self.fail("Logo not found or not visible")

        # Check main menu links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Main menu links not found or not visible")

        # Check account buttons
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Account buttons not found or not visible")

        # Check cart icon
        try:
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.icon-cart")))
        except:
            self.fail("Cart icon not found or not visible")

        # Check footer elements
        try:
            footer_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.footer-logo img")))
            contact_info = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'1234 Street address')]")))
        except:
            self.fail("Footer elements not found or not visible")

        # Check subscribe form
        try:
            subscribe_input = wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "input[name='email']")))
            subscribe_button = wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "button.button")))
        except:
            self.fail("Subscribe form elements not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()