from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_components_present(self):
        # Check header presence
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'nav')))
        self.failUnless(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav')))

        # Check button presence ( login and register)
        buttons = [EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")),
                   EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/registration']"))]
        for button in buttons:
            self.failUnless(button)

        # Check links presence (home, clothes, accessories, art)
        links = [EC.element_to_be_clickable((By.LINK_TEXT, "Home")),
                 EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")),
                 EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")),
                 EC.element_to_be_clickable((By.LINK_TEXT, "Art"))]
        for link in links:
            self.failUnless(link)

    def test_links_visible(self):
        # Check header visibility
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav')))

        # Check buttons visibility
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))

        # Check links visibility
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Art")))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()