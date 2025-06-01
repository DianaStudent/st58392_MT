from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestShopizerUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//header//a[@href='/']")))
        except:
            self.fail("Logo link not visible")

        # Verify navigation links
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Navigation links not visible")

        # Verify login and register links
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/login']")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/register']")))
        except:
            self.fail("Login/Register links not visible")

        # Verify product elements
        try:
            product_selector = "//a[contains(@href, '/product/')]"
            self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, product_selector)))
        except:
            self.fail("Products not visible")

        # Verify footer elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//footer//a[@href='/contact']")))
        except:
            self.fail("Footer link not visible")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()