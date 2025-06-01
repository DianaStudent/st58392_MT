import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def setUp(self):
self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
self.wait = WebDriverWait(self.driver, 20)

def tearDown(self):
self.driver.quit()

class TestFiltering(unittest.TestCase):

def test_filter_tables(self):
self.wait.until(EC.element_clickable(by=By.XPATH, "//button[contains(text()='Tables')]"))
self.wait.until(EC.text_to_be("All"))
self.assertEqual(len(self.driver.find_elements(by=By.XPATH, "//li[contains(@data-id)]//img[contains(@src)][contains(@alt,'Brown Leather Chair with smooth surface')]")),1)

def test_filter_chairs(self):
self.wait.until(EC.element_clickable(by=By.XPATH, "//button[contains(text(),'Tables')]"))
self.wait.until(EC.text_to_be("All"))
self.wait.until(EC.element_clickable(by=By.XPATH, "//button[contains(text(),'Chairs')}")
self.assertEqual(len(self.driver.find_elements(by=By.XPATH, "//li[contains(@data-id)]//img[contains(@src)][contains(@alt,'Brown Leather Chair with smooth surface')]")),1)

def test_filter_all(self):
self.wait.until(EC.element_clickable(by=By.XPATH, "//button[contains(text(),'Tables')}")
self.assertEqual(len(self.driver.find_elements(by=By.XPATH, "//li[contains(@data-id)]//img[contains(@src)][contains(@alt,'Brown Leather Chair with smooth surface)]")),0)

if __name__ == '__main__':
unittest.main()