import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIComponents(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header area not found or not visible.")

        # Check for navigation links in the header
        try:
            nav_links = header.find_elements(By.TAG_NAME, "a")
            home_link = next(link for link in nav_links if link.get_attribute('href') == "http://localhost/")
            tables_link = next(link for link in nav_links if link.get_attribute('href') == "http://localhost/category/tables")
            chairs_link = next(link for link in nav_links if link.get_attribute('href') == "http://localhost/category/chairs")
        except StopIteration:
            self.fail("One or more navigation links not found or not visible.")

        # Check for login and register links
        try:
            account_dropdown_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
            account_dropdown_button.click()

            login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/login']")))
            register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/register']")))
        except:
            self.fail("Login/Register links not found or not visible.")

        # Check for main menu nav items
        try:
            nav_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "nav ul li a")))
        except:
            self.fail("Main menu navigation items not found or not visible.")

        # Check for product categories and products
        try:
            container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.container")))
            product_images = container.find_elements(By.CSS_SELECTOR, "img.default-img")
        except:
            self.fail("Product images not found or not visible.")

        if not product_images:
            self.fail("No product images found on the page.")

if __name__ == "__main__":
    unittest.main()