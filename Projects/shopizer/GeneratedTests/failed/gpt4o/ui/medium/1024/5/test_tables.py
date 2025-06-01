from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver

        # Check navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Home']")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Tables']")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Chairs']")))
        except:
            self.fail("Navigation links are not present or visible")

        # Check login and register links
        try:
            login_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/login']")))
            register_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/register']")))
        except:
            self.fail("Login or Register links are not present or visible")

        # Check elements in the cookie consent banner
        try:
            consent_banner = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "CookieConsent")))
            accept_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except:
            self.fail("Cookie consent banner or accept button is not present or visible")
        
        # Check presence of a product and its action buttons
        try:
            product = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h3/a[text()='Olive Table']")))
            add_to_cart_button = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='pro-same-action pro-cart']/button[text()=' Add to cart']")))
        except:
            self.fail("Product or Add to cart button is not present or visible")

        # Interact with the "Add to cart" button
        try:
            add_to_cart_button.click()
        except:
            self.fail("Clicking on Add to cart button caused an error")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()