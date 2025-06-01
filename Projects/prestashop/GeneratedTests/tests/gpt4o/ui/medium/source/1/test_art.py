import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/9-art")

    def test_ui_elements(self):
        driver = self.driver

        # Check navigation links
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']"))
            )
        except:
            self.fail("Home link not found or not visible.")

        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']"))
            )
        except:
            self.fail("Clothes link not found or not visible.")

        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']"))
            )
        except:
            self.fail("Accessories link not found or not visible.")

        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
            )
        except:
            self.fail("Art link not found or not visible.")

        # Check form inputs
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @name='s']"))
            )
        except:
            self.fail("Search input not found or not visible.")
        
        # Check buttons
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@type='submit' and @name='submitNewsletter']"))
            )
        except:
            self.fail("Subscribe button not found or not visible.")

        # Check banner/image
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//img[@alt='Art']"))
            )
        except:
            self.fail("Art banner image not found or not visible.")
        
        # Interact with elements
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='header']//i[text()='shopping_cart']"))
            )
            cart_button.click()
        except:
            self.fail("Shopping cart button not found or not clickable.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()