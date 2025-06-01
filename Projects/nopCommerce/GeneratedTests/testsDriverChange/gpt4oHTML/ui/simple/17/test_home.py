import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestWebUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check that the elements in the header are present and visible
        try:
            header_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header-logo a img")))
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@class, 'ico-login')]")))
            register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@class, 'ico-register')]")))

            # Ensure these elements are not None
            self.assertIsNotNone(header_logo)
            self.assertIsNotNone(search_box)
            self.assertIsNotNone(login_button)
            self.assertIsNotNone(register_button)
        
        except Exception as e:
            self.fail(f"Header UI components not found: {e}")

        # Check that the menu links are present and visible
        try:
            menu_links = [
                "//ul[@class='top-menu notmobile']/li/a[text()='Home page']",
                "//ul[@class='top-menu notmobile']/li/a[text()='New products']",
                "//ul[@class='top-menu notmobile']/li/a[text()='Search']",
                "//ul[@class='top-menu notmobile']/li/a[text()='My account']",
                "//ul[@class='top-menu notmobile']/li/a[text()='Blog']",
                "//ul[@class='top-menu notmobile']/li/a[text()='Contact us']"
            ]

            for link_xpath in menu_links:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, link_xpath)))
                self.assertIsNotNone(element)
        
        except Exception as e:
            self.fail(f"Menu links not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()