from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_shop_react_app(self):
        # Open the page.
        self.driver.get("http://localhost/")

        # Confirm the presence of key interface elements
        self.failUnlessElementExists(By.XPATH, "//nav[@class='navbar navbar-expand-lg navbar-light bg-light']")
        self.failUnlessElementExists(By.XPATH, "//input[@type='text']")
        self.failUnlessElementExists(By.XPATH, "//button[@type='submit']")

        # Interact with one or two elements.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        # Verify that interactive elements do not cause errors in the UI.
        self.failUnlessElementExists(By.XPATH, "//h1")

    def tearDown(self):
        self.driver.quit()

    @staticmethod
    def failUnlessElementExists(by_locator):
        try:
            WebDriverWait(TestShopReactApp.driver, 20).until(EC.element_to_be_clickable(by_locator))
        except Exception as e:
            raise AssertionError(f"Element {by_locator} does not exist: {str(e)}")

if __name__ == "__main__":
    unittest.main()