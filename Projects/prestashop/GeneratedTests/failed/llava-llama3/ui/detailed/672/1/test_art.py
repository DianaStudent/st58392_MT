from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions import Key, Action
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebPage(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        driver_path = "chromedriver"
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_path)
        
    def tearDown(self):
        self.driver.quit()

    def test_load_page(self):
        url = "http://localhost:8080/en/"
        self.driver.get(url)

        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//header")))
        navigation = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//nav[@role='navigation']")))

    def test_interact_with_ui_elements(self):
        art_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(By.XPATH, "//a[@href='/en/9-art']"))
        self.assertEqual(art_tab.get_attribute("href"), "http://localhost:8080/en/9-art")

if __name__ == '__main__':
    unittest.main()