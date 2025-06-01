from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):

    def setUp(self):
        self.driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Ensure structural elements are visible
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
            self.assertTrue(header.is_displayed(), "Header is not displayed")
            self.assertTrue(footer.is_displayed(), "Footer is not displayed")
        except:
            self.fail("Failed to display header or footer.")

        # Check input fields, buttons, labels, and sections
        try:
            login_link = driver.find_element(By.CLASS_NAME, 'ico-login')
            register_link = driver.find_element(By.CLASS_NAME, 'ico-register')
            search_box = driver.find_element(By.ID, 'small-searchterms')
            search_button = driver.find_element(By.CSS_SELECTOR, 'button.search-box-button')
            cart_link = driver.find_element(By.ID, 'topcartlink')

            self.assertTrue(login_link.is_displayed(), "Login link is not displayed")
            self.assertTrue(register_link.is_displayed(), "Register link is not displayed")
            self.assertTrue(search_box.is_displayed(), "Search box is not displayed")
            self.assertTrue(search_button.is_displayed(), "Search button is not displayed")
            self.assertTrue(cart_link.is_displayed(), "Cart link is not displayed")
        except:
            self.fail("One of the key UI elements is missing or not visible.")

        # Interact with UI elements
        try:
            login_link.click()
            self.wait.until(EC.url_contains("login"))
            driver.back()

            register_link.click()
            self.wait.until(EC.url_contains("register"))
            driver.back()

            search_box.send_keys("test product")
            search_button.click()
            self.wait.until(EC.url_contains("search"))
        except:
            self.fail("Failed to interact with UI elements as expected.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()