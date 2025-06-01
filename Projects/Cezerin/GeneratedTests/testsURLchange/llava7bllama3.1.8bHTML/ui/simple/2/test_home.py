import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_main_ui_components(self):
        # Navigate to the webpage
        self.driver.get("http://example.com")

        # Wait for 20 seconds before interacting with elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "header")))

        # Check that main UI components are present
        self.failUnlessElementPresent(By.CSS_SELECTOR, "header")
        self.failUnlessElementPresent(By.CSS_SELECTOR, "#category_a .title")
        self.failUnlessElementPresent(By.XPATH, "//button[@class='add-to-cart']")
        self.failUnlessElementPresent(By.LINK_TEXT, "View more")

        # Check that elements are visible
        self.failUnlessElementVisible(By.CSS_SELECTOR, "header")
        self.failUnlessElementVisible(By.CSS_SELECTOR, "#category_a .title")
        self.failUnlessElementVisible(By.XPATH, "//button[@class='add-to-cart']")
        self.failUnlessElementVisible(By.LINK_TEXT, "View more")

    def failUnlessElementPresent(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        if not element:
            self.fail(f"Required element {locator} is missing.")

    def failUnlessElementVisible(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        if not element:
            self.fail(f"Required element {locator} is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()