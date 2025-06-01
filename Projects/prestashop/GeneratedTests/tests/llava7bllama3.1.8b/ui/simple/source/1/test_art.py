import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestWebshop(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:8080/en/")

    def test_main_page_elements(self):
        # Check header elements
        header_elements = ['h1', 'h2']
        for element in header_elements:
            element_xpath = f"//{element}"
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
        
        # Check main page buttons and links
        main_buttons = ['button', 'a']
        for button_or_link in main_buttons:
            if button_or_link == 'button':
                self.driver.find_element(By.TAG_NAME, button_or_link).is_displayed()
            else:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, button_or_link)))
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()