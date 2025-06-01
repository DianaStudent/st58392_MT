```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alerts import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.actions import Key, ClickAction, MoveAction
from selenium.webdriver.common.actions import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxLoginRegisterSearch(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver_path())
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_max_login_register_search(self):
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'header')][1]"))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'login')]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'email')]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[contains(action='POST')][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'password')]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[contains(action='POST')][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'email')]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'password)]")""))))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'submit)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[contains(action='POST')][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'email)]")""))))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'password)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'submit)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[contains(action='POST')][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'email)]")""))))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'password)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'submit)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[contains(action='POST')][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'email)]")""))))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'password)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'submit)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[contains(action='POST')][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'email)]")""))))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'password)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'submit)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[contains(action='POST')][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'email)]")""))))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'password)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'submit)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[contains(action='POST')][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'email)]")""))))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'password)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'submit)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[contains(action='POST')][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'email)]")""))))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'password)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'submit)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[contains(action='POST')][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'email)]")""))))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'password)][1]")))))
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text,','
```