from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_components(self):
        driver = self.driver
        wait = self.wait

        # Check header presence
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header is not present or visible.")
        
        # Check navigation links
        nav_links = ["Home", "Tables", "Chairs", "Login", "Register"]
        for link in nav_links:
            try:
                nav_link = wait.until(EC.visibility_of_element_located(
                    (By.LINK_TEXT, link)))
            except:
                self.fail(f"Navigation link '{link}' is not present or visible.")

        # Check 'Accept cookies' button presence
        try:
            accept_button = wait.until(EC.visibility_of_element_located(
                (By.ID, "rcc-confirm-button")))
        except:
            self.fail("'Accept cookies' button is not present or visible.")
        
        # Check product addition to cart buttons
        try:
            add_to_cart_buttons = wait.until(EC.visibility_of_all_elements_located(
                (By.XPATH, "//button[contains(text(), 'Add to cart')]")))
        except:
            self.fail("Add to cart buttons are not present or visible.")
        
        # Check footer presence
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer is not present or visible.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()