import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_main_components(self):
        # Header exists and is visible
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))
        self.assertEqual(header.is_displayed(), True)

        # Navigation links exist and are visible
        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='nav']//li/a")))
        for link in nav_links:
            self.assertEqual(link.is_displayed(), True)
            if "Clothes" in link.get_attribute("href"):
                continue
            elif "Accessories" in link.get_attribute("href"):
                continue
            elif "Art" in link.get_attribute("href"):
                continue

        # Main buttons exist and are visible
        main_buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//button")))
        for button in main_buttons:
            self.assertEqual(button.is_displayed(), True)

    def test_login_link(self):
        login_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        self.assertEqual(login_link.is_displayed(), True)

    def test_register_link(self):
        register_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        self.assertEqual(register_link.is_displayed(), True)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()