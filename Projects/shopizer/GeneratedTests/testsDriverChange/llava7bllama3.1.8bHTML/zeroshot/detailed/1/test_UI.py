import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopReact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_shop_react(self):
        # Load the home page and ensure that structural elements are visible
        self.driver.get("http://localhost/")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='navbar-toggler']"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "header"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "footer"))
        )

        # Check the presence and visibility of input fields, buttons, labels, and sections
        self.failUnlessElementPresent(By.XPATH, "//input[@name='search']")
        self.failUnlessElementPresent(By.XPATH, "//button[@class='btn btn-primary']")
        self.failUnlessElementPresent(By.TAG_NAME, "form")

        # Interact with key UI elements (e.g., click buttons)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
        ).click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        self.assertEqual("Tables | Shop React", self.driver.title)

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
        ).click()
        self.assertEqual("Chairs | Shop React", self.driver.title)

    def failUnlessElementPresent(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            self.assertTrue(element.is_displayed())
        except TimeoutException:
            self.fail(f"Element not found: {locator}")

if __name__ == "__main__":
    unittest.main()