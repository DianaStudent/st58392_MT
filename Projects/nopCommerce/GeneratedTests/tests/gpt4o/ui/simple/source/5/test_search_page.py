import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestSearchPageUIElements(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("http://max/search")

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='header-logo']/a/img")))
        except:
            self.fail("Header logo is not visible.")

        # Check search box
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        except:
            self.fail("Search box is not visible.")

        # Check search button
        try:
            search_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'search-box-button')]")))
        except:
            self.fail("Search button is not visible.")

        # Check registration link
        try:
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Register link is not visible.")

        # Check login link
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
        except:
            self.fail("Login link is not visible.")

        # Check footer links
        try:
            footer_links = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='footer-upper']//ul[@class='list']")))
        except:
            self.fail("Footer links are not visible.")
             
        # Check product items
        try:
            product_items = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-item")))
        except:
            self.fail("Product items are not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()