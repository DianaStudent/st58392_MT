from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UIElementsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header and navigation links
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
            home_link = header.find_element(By.LINK_TEXT, 'Home')
            tables_link = header.find_element(By.LINK_TEXT, 'Tables')
            chairs_link = header.find_element(By.LINK_TEXT, 'Chairs')
        except:
            self.fail("Header or navigation links are not present or visible.")

        # Check for the search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="email"]')))
        except:
            self.fail("Search input is not present or visible.")

        # Check for the 'Accept Cookies' button
        try:
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        except:
            self.fail("Accept Cookies button is not present or visible.")

        # Check a product button and click to verify functionality
        try:
            add_to_cart_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Add to cart")]')))
            add_to_cart_button.click()
            cart_content = wait.until(EC.visibility_of_element_located((By.XPATH, '//p[contains(text(), "No items added to cart")]')))
        except:
            self.fail("Product button interaction failed or cart update failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()