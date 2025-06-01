import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost/")

    def test_shop_react_app(self):
        # Verify the presence of key interface elements: navigation links, inputs, buttons, banners
        self.failUnlessPresent(By.XPATH, "//header[@class='App-header']", "Header")
        self.failUnlessPresent(By.LINK_TEXT, "Tables", "Navigation link: Tables")
        self.failUnlessPresent(By.LINK_TEXT, "Chairs", "Navigation link: Chairs")
        self.failUnlessPresent(By.ID, "input-field", "Input field")
        self.failUnlessPresent(By.XPATH, "//button[@type='submit']", "Submit button")

        # Interact with one or two elements — e.g., click a button and check that the UI updates visually
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//p[@class='App-intro']")))

        # Verify that interactive elements do not cause errors in the UI
        self.failUnlessPresent(By.XPATH, "//p[@class='App-intro']", "Paragraph with App intro text")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()