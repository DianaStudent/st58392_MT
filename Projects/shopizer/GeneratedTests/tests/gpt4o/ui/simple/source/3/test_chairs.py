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

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        # Check for header elements
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area"))
                            , message="Header not visible")
        
        # Check for navigation links
        nav_links = ["Home", "Tables", "Chairs"]
        for link_text in nav_links:
            link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text))
                              , message=f"Navigation link '{link_text}' not visible")

        # Check for cookie consent button
        cookie_consent = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
                                    , message="Cookie consent button not visible")
        
        # Check for login and register links
        account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active"))
                                    , message="Account settings button not visible")
        account_button.click()
        
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
                                , message="Login link not visible")
        
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register"))
                                   , message="Register link not visible")

        # Check for cart icon
        cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart"))
                               , message="Cart icon not visible")
        
        # Check for product elements
        products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap"))
                              , message="Products not visible")
        # At least one product should be present
        if len(products) < 1:
            self.fail("Expected at least one product to be visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()