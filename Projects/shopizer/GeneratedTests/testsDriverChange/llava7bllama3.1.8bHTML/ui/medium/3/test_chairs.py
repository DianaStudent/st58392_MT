import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements_presence(self):
        # Navigation links
        navigation_links = (By.XPATH, "//nav//a")
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(navigation_links))
        
        # Inputs
        input_fields = (By.XPATH, "//input[@type='text']")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(input_fields))
        
        # Buttons
        buttons = (By.XPATH, "//button")
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(buttons))
        
        # Banners
        banners = (By.XPATH, "//h1[@class='page-title']")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(banners))

    def test_interactive_element_click(self):
        buttons = (By.XPATH, "//button")
        button_element = self.driver.find_element(*buttons)[0]
        button_element.click()
        
        # Verify UI updates visually
        new_element = (By.XPATH, "//p[@class='updated-message']")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(new_element))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()