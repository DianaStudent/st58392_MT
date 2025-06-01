import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        driver = self.driver
        wait = self.wait

        try:
            # Header
            wait.until(EC.visibility_of_element_located((By.ID, "header")))

            # Main Categories
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Login and Register Links
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))

            # Search Bar
            wait.until(EC.visibility_of_element_located((By.NAME, "s")))

            # Cart
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".blockcart.cart-preview.inactive")))

            # Footer
            wait.until(EC.visibility_of_element_located((By.ID, "footer")))

            # Newsletter Form
            wait.until(EC.visibility_of_element_located((By.NAME, "email")))

        except Exception as e:
            self.fail(f"Failed to verify one or more UI components: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()