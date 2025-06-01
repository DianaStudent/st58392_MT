import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Verify navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
        except:
            self.fail("Home link is not visible")

        try:
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
        except:
            self.fail("Clothes link is not visible")
        
        try:
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
        except:
            self.fail("Accessories link is not visible")
        
        try:
            art_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        except:
            self.fail("Art link is not visible")

        # Verify header presence
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible")

        # Verify contact link
        try:
            contact_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/contact-us']")))
        except:
            self.fail("Contact us link is not visible")
        
        # Verify search input
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text'][@name='s']")))
        except:
            self.fail("Search input is not visible")

        # Verify products section
        try:
            products_section = self.wait.until(EC.visibility_of_element_located((By.ID, "products")))
        except:
            self.fail("Products section is not visible")
        
        # Interact with an element - click one of the products
        try:
            first_product = self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(@href, '/en/art/')])[1]")))
            first_product.click()
        except:
            self.fail("Failed to click the first product")
        
        # Verify it leads to the correct page
        self.assertTrue("http://localhost:8080/en/art/" in driver.current_url, "Redirect did not occur to product page after clicking")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()