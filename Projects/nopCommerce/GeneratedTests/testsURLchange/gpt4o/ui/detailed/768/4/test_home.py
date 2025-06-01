import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        # Set up ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_home_page_elements(self):
        driver = self.driver
        driver.get("http://max/")

        wait = WebDriverWait(driver, 20)

        # Check Header
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        if not header.is_displayed():
            self.fail("Header not visible")

        # Check Footer
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        if not footer.is_displayed():
            self.fail("Footer not visible")

        # Check Navigation Links
        top_menu = driver.find_element(By.CLASS_NAME, "top-menu")
        links = top_menu.find_elements(By.TAG_NAME, "a")
        if not links:
            self.fail("Navigation links not found")

        # Check Search Box
        search_box_form = wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
        search_input = search_box_form.find_element(By.ID, "small-searchterms")
        search_button = search_box_form.find_element(By.CLASS_NAME, "search-box-button")
        if not (search_input.is_displayed() and search_button.is_displayed()):
            self.fail("Search input or button not visible")

        # Interact with Search
        search_input.send_keys("test")
        search_button.click()

        # Check Login Link
        login_link = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ico-login")))
        if not login_link.is_displayed():
            self.fail("Login link not visible")

        # Check Register Link
        register_link = driver.find_element(By.CLASS_NAME, "ico-register")
        if not register_link.is_displayed():
            self.fail("Register link not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()