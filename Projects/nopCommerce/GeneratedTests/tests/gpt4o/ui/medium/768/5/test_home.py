import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence_and_interaction(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Confirm the presence of header links
        self.verify_element_presence(wait, By.LINK_TEXT, "Register")
        self.verify_element_presence(wait, By.LINK_TEXT, "Log in")
        self.verify_element_presence(wait, By.LINK_TEXT, "Shopping cart")
        
        # Confirm the presence of search box and button
        search_box = self.verify_element_presence(wait, By.ID, "small-searchterms")
        search_btn = self.verify_element_presence(wait, By.CLASS_NAME, "search-box-button")
        
        # Confirm the presence of navigation menu
        self.verify_element_presence(wait, By.LINK_TEXT, "Home page")
        self.verify_element_presence(wait, By.LINK_TEXT, "New products")
        self.verify_element_presence(wait, By.LINK_TEXT, "Contact us")
        
        # Confirm the presence of banners
        banners = self.verify_element_presence(wait, By.CLASS_NAME, "swiper-slide")
        
        # Interact with search box and button
        search_box.send_keys("Test")
        search_btn.click()

        # Verify interaction does not cause errors
        try:
            wait.until(EC.url_contains("search?q=Test"))
        except:
            self.fail("Interacting with search did not redirect properly.")

    def verify_element_presence(self, wait, by, value):
        try:
            element = wait.until(EC.visibility_of_element_located((by, value)))
            return element
        except:
            self.fail(f"Element with locator ({by}, {value}) not present or visible.")

if __name__ == "__main__":
    unittest.main()