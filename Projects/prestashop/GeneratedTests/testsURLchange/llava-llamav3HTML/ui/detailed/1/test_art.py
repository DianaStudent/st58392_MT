```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestPrestashopStore(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_prestashop_store(self):
        # Load the page
        base_url = "http://localhost:8080/en/"
        self.driver.get(base_url)

        # Test scenario 1: Check presence and visibility of main UI components

        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                                     "//html/body/\
                                                                                      <head/>\
                                                                                      <title>Online store for fashion products - Prestashop</title>\
                                                                                      <meta charset=\"utf-8\"/>\
                                                                                      <meta name=\"robots\" content=\"noindex, nofollow\"/>\
                                                                                      <title>Boutique en ligne de vêtements pour femmes - Vêtements de qualité à prix raisonnable. Vêtements de toutes tailles et tous styles | Prestashop | Boutique de vêtements</title>"))))

        navigation = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                                     "//nav[contains(@role,\"navigation\")]")))

        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                                     "//div[contains(@class,\"panel-body panel-collapse ng-scope\") and contains(@role,\"collapsable\")]/div")));

        # Test scenario 2: Interact with key UI elements

        button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                                     "//button[contains(text,\"Login\")]")))

        self.assertEqual(button.get_attribute("value"), "Login", msg="Button is missing label")

        # Test scenario 3: Confirm that the UI reacts visually

        self.wait_for_page_to_load()

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                     "//input[contains(@class,\"form-control\")]"))))

if __name__ == '__main__':
    unittest.main()
```