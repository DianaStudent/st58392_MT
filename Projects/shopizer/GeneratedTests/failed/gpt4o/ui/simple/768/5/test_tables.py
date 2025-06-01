from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestShopPageElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver

        # Check for header elements
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Home']")))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Tables']")))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Chairs']")))

        # Check for login and register links
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Login']")))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Register']")))

        # Check for product elements
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h3/a[text()='Olive Table']")))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h3/a[text()='Chair']")))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h3/a[text()='Chair Beige']")))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h3/a[text()='Genuine Chair']")))

        # Check for footer
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()