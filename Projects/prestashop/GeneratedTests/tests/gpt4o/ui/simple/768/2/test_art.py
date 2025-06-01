import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ArtPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_presence_and_visibility(self):
        driver = self.driver

        try:
            # Check header presence and visibility
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header#header")))

            # Check navigation links
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/contact-us']")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")))

            # Check cart presence
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.material-icons.shopping-cart")))

            # Check search bar presence
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form[action='//localhost:8080/en/search']")))

            # Check for product list
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "section#products")))

            # Check footer presence
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer#footer")))

        except Exception as e:
            self.fail(f"Test failed due to missing or invisible element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()