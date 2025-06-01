from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.title import Title
from selenium.webdriver.support.wait import WaitUntil
from selenium.webdriver.support.assertions import Assert

class ShopperWebsiteTest(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.url = "http://localhost/"
        
    def tearDown(self):
        self.driver.quit()
    
    def test_shopper_1_chairs(self):
        self.driver.get(self.url + "category/chairs")
        assert(self.driver.title. == "Chairs - Shopper")
        chair_dining = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Dining Chair')]")))
        assert(chair_dining.is_displayed())
        
    def test_shopper_2_chairs(self):
        self.driver.get(self.url + "category/chairs")
        assert(self.driver.title. == "Chairs - Shopper")
        chair_sofa = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Sofa Chair')]")))
        assert(chair_sofa.is_displayed())
        
    def test_login(self):
        self.driver.get(self.url + "login")
        username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "username")))
        password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "password")))
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
        WebDriverWait(self.driver, 20).until(
            EC.url_to_be(self.url + "dashboard"))
        
    def test_register(self):
        self.driver.get(self.url + "register")
        email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "email")))
        username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "username")))
        password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "password")))
        register_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Register')]")))
        WebDriverWait(self.driver, 20).until(
            EC.url_to_be(self.url + "dashboard"))