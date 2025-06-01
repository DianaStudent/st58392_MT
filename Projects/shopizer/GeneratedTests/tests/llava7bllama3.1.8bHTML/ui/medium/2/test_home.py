import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopReactApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.get("http://localhost/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_shopreactapp(self):
        # Confirm the presence of key interface elements
        self.check_elementPresence(By.XPATH, "//div[@class='nav-links']")
        self.check_elementPresence(By.XPATH, "//input[@name='searchInput']")
        self.check_elementPresence(By.XPATH, "//button[@type='submit']")

        # Interact with one or two elements
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Success')]")))

    def check_elementPresence(self, locatorType, locator):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((locatorType, locator)))
            self.assertTrue(element.is_displayed())
        except TimeoutException:
            self.fail(f"Element {locator} not found")

if __name__ == '__main__':
    unittest.main()