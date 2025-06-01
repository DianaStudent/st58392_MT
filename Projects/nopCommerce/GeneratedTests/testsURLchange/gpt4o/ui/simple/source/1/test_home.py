import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UIElementsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header-upper")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/register?returnUrl=%2F']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/login?returnUrl=%2F']")))
        except:
            self.fail("Header elements are missing or not visible.")

        # Check main UI components
        try:
            # Logo
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header-logo a img")))

            # Search box
            wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button")))

            # Main menu
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.top-menu.notmobile")))

            # Footer
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.footer")))

            # Newsletter
            wait.until(EC.visibility_of_element_located((By.ID, "newsletter-email")))
            wait.until(EC.visibility_of_element_located((By.ID, "newsletter-subscribe-button")))
        except:
            self.fail("Main UI components are missing or not visible.")

        # Check that menu links are visible
        menu_links = ["/", "/newproducts", "/search", "/customer/info", "/blog", "/contactus"]
        for href in menu_links:
            try:
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"ul.top-menu.notmobile a[href='{href}']")))
            except:
                self.fail(f"Menu link {href} is missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()