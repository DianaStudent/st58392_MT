import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.credentials = {
            "gender": "F",
            "first_name": "Test",
            "last_name": "User",
            "company": "TestCorp",
            "password": "test11"
        }

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        # 1. Open the homepage.
        home_page_html = "<body style=\"zoom: 50%;\"> <div class=\"master-wrapper-page\"> <div class=\"header\"> <a class=\"skip\" href=\"#main\">Skip navigation</a> <div class=\"header-upper\"> <div class=\"header-links-wrapper\"> <div class=\"flyout-cart\" id=\"flyout-cart\"> <div class=\"mini-shopping-cart\"> <div class=\"count\"> You have no items in your shopping cart. </div> </div> </div> </div> </div> <div class=\"header-lower\"> <div class=\"header-logo\"> <a href=\"/\"> <img alt=\"Your store name\" src=\"http://max/Themes/DefaultClean/Content/images/logo.png\" title=\"\"/> </a> </div> <div class=\"search-box store-search-box\"> <form action=\"/search\" id=\"small-search-box-form\" method=\"get\"> <input aria-label=\"Search store\" autocomplete=\"off\" class=\"search-box-text ui-autocomplete-input\" id=\"small-searchterms\" name=\"q\" placeholder=\"Search store\" type=\"text\"/> <button class=\"button-1 search-box-button\" type=\"submit\">Search</button> </form> </div> </div> </div> <div class=\"header-menu\"> <ul class=\"top-menu notmobile\"> <li><a href=\"/\">Home page</a></li> <li><a href=\"/newproducts\">New products</a></li> <li><a href=\"/search\">Search</a></li> <li><a href=\"/customer/info\">My account</a></li> <li><a href=\"/blog\">Blog</a></li> <li><a href=\"/contactus\">Contact us</a></li> </ul> <div aria-controls=\"aria-categories-mobile-ul\" class=\"menu-toggle\" role=\"button\" tabindex=\"0\">Menu</div> <ul class=\"top-menu mobile\"> <li><a href=\"/\">Home page</a></li> <li><a href=\"/newproducts\">New products</a></li> <li><a href=\"/search\">Search</a></li> <li><a href=\"/customer/info\">My account</a></li> <li><a href=\"/blog\">Blog</a></li> <li><a href=\"/contactus\">Contact us</a></li> </ul> </div> </div> </body>"
        # 2. Click the "Register" link in the top navigation.
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Register' link: {e}")

        # 3. Wait for the registration form to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "registration-page"))
            )
        except Exception as e:
            self.fail(f"Registration form did not load: {e}")

        # 4. Select the appropriate gender radio input based on the provided data.
        gender = self.credentials["gender"]
        gender_id = "gender-female" if gender == "F" else "gender-male"
        try:
            gender_radio = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, gender_id))
            )
            gender_radio.click()
        except Exception as e:
            self.fail(f"Could not select gender: {e}")

        # 5. Fill in all required fields: first name, last name, email, company name, password, confirm password from credentials.
        first_name = self.credentials["first_name"]
        last_name = self.credentials["last_name"]
        email = f"testuser_{uuid.uuid4()}@example.com"
        company = self.credentials["company"]
        password = self.credentials["password"]

        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            first_name_input.send_keys(first_name)

            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            last_name_input.send_keys(last_name)

            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys(email)

            company_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            )
            company_input.send_keys(company)

            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys(password)

            confirm_password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password_input.send_keys(password)

        except Exception as e:
            self.fail(f"Could not fill in registration form: {e}")

        # 6. Submit the registration form.
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "register-button"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Could not submit registration form: {e}")

        # 7. Wait for the response page or confirmation message to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "registration-result-page"))
            )
        except Exception as e:
            self.fail(f"Registration result page did not load: {e}")

        # 8. Verify that registration succeeded by checking:
        #    - A confirmation text element is present - Its content includes "Your registration completed".
        try:
            confirmation_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            )
            confirmation_text = confirmation_message.text
            self.assertIn("Your registration completed", confirmation_text, "Registration confirmation message is incorrect.")
        except Exception as e:
            self.fail(f"Could not verify registration success: {e}")

if __name__ == "__main__":
    unittest.main()