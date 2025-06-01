import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestArtPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify header links
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))

            # Verify login and register buttons
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))

            # Verify search field
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search our catalog']")))

            # Verify product list
            products = [
                "http://localhost:8080/en/art/3-13-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm",
                "http://localhost:8080/en/art/4-16-the-adventure-begins-framed-poster.html#/19-dimension-40x60cm",
                "http://localhost:8080/en/art/5-19-today-is-a-good-day-framed-poster.html#/19-dimension-40x60cm",
                "http://localhost:8080/en/art/12-mountain-fox-vector-graphics.html",
                "http://localhost:8080/en/art/13-brown-bear-vector-graphics.html",
                "http://localhost:8080/en/art/14-hummingbird-vector-graphics.html",
                "http://localhost:8080/en/home-accessories/15-pack-mug-framed-poster.html"
            ]
            for product in products:
                wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{product}']")))

            # Verify footer subscription form
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Your email address']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='submitNewsletter']")))

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()