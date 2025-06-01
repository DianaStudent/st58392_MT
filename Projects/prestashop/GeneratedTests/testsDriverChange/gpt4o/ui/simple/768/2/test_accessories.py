import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_UI_elements_present_and_visible(self):
        driver = self.driver

        # Check header elements
        self.assert_element_visible(By.ID, "header")
        self.assert_element_visible(By.XPATH, "//a[@href='http://localhost:8080/en/']")
        
        # Check navigation links
        self.assert_element_visible(By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")
        self.assert_element_visible(By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")

        # Check user login/register links
        self.assert_element_visible(By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F6-accessories']")
        self.assert_element_visible(By.XPATH, "//a[@href='http://localhost:8080/en/registration']")

        # Check main content elements
        self.assert_element_visible(By.CLASS_NAME, "h1")
        self.assert_element_visible(By.XPATH, "//div[@id='js-product-list']")

        # Check product elements
        product_links = driver.find_elements(By.XPATH, "//div[@class='js-product']//a[@class='thumbnail product-thumbnail']")
        self.assertTrue(len(product_links) > 0, "No product links found.")

    def assert_element_visible(self, by, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            self.assertTrue(element.is_displayed(), f'Element not visible: {value}')
        except Exception as e:
            self.fail(f'Element not found or visible: {value} - {str(e)}')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()