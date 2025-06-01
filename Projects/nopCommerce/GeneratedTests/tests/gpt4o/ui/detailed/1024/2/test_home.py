import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://max/")

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except:
            self.fail("Header is not visible on the page.")

        # Check footer visibility
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        except:
            self.fail("Footer is not visible on the page.")

        # Check navigation menu visibility
        try:
            navigation_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-menu")))
        except:
            self.fail("Top navigation menu is not visible on the page.")

        # Check search box visibility
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        except:
            self.fail("Search box or button is not visible on the page.")

        # Check login and register links
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-login")))
            register_link = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-register")))
        except:
            self.fail("Login or Register link is not visible on the page.")

        # Interact with search box
        search_box.send_keys("test")
        search_button.click()

        # Wait for search page navigation
        try:
            wait.until(EC.url_contains("search"))
        except:
            self.fail("Search operation did not navigate to search page.")

        # Check shopping cart link
        try:
            cart_link = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-cart")))
            cart_link.click()
        except:
            self.fail("Shopping cart link is not visible or clickable.")

        # Confirm UI reacts visually by checking cart page
        try:
            wait.until(EC.url_contains("cart"))
        except:
            self.fail("Clicking on shopping cart link did not navigate to cart page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()