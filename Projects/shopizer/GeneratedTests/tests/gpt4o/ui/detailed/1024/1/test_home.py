import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver

        # Verify header is present and visible
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, "header"))
        )
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verify footer is present and visible
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, "footer"))
        )
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check navigation links
        elements = {
            "home_link": (By.XPATH, "//a[@href='/']"),
            "tables_link": (By.XPATH, "//a[@href='/category/tables']"),
            "chairs_link": (By.XPATH, "//a[@href='/category/chairs']"),
            "login_link": (By.XPATH, "//a[@href='/login']"),
            "register_link": (By.XPATH, "//a[@href='/register']")
        }
        
        for name, locator in elements.items():
            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(locator))
            self.assertTrue(elem.is_displayed(), f"{name} is not visible")
        
        # Verify cookie consent button and interact
        cookie_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
        )
        self.assertTrue(cookie_button.is_displayed(), "Cookie consent button is not visible")
        cookie_button.click()

        # Check product section and product images
        product_section = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "product-area"))
        )
        self.assertTrue(product_section.is_displayed(), "Product section is not visible")

        product_images = driver.find_elements(By.CLASS_NAME, "product-img")
        self.assertGreater(len(product_images), 0, "Product images are missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()