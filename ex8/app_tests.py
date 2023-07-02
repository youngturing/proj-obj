import unittest
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class TestCases(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.implicitly_wait(10) 

    def test_title(self):
        self.assertEqual(self.driver.title, "Contact List App")
    
    def test_submit_button(self):
        submit_button = self.driver.find_element(By.ID, ("submit"))
        self.assertTrue(submit_button.is_displayed())

    def test_signup_button(self):
        signup_button = self.driver.find_element(By.ID, ("signup"))
        self.assertTrue(signup_button.is_displayed())

    def test_submit_button_text(self):
        submit_button = self.driver.find_element(By.ID, ("submit"))
        button_text = submit_button.text
        self.assertEqual(button_text, 'Submit')

    def test_submit_button_text(self):
        signup_button = self.driver.find_element(By.ID, ("signup"))
        button_text = signup_button.text
        self.assertEqual(button_text, 'Sign up')

    def test_incorrect_login_no_data_status(self):
        response = requests.post('https://thinking-tester-contact-list.herokuapp.com/users/login')
        self.assertEqual(response.status_code, 401)

    def test_incorrect_login_no_data_message_displayed(self):
        submit_button = self.driver.find_element(By.ID, ("submit"))
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        self.assertTrue(error_message.is_displayed())

    def test_incorrect_login_no_data_message_text(self):
        submit_button = self.driver.find_element(By.ID, ("submit"))
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        self.assertEqual(error_message.text, "Incorrect username or password")

    def test_incorrect_signup_message_displayed(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        self.assertTrue(error_message.is_displayed())

    def test_incorrect_signup_message_text(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        self.assertEqual(
            error_message.text, "User validation failed: firstName: Path `firstName` is required., lastName: Path `lastName` is required., email: Email is invalid, password: Path `password` is required."
        )

    def test_incorrect_signup_message_fname_displayed(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        fname_input = self.driver.find_element(By.ID, "firstName")
        fname_input.send_keys("Name")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        
        self.assertTrue(error_message.is_displayed())

    def test_incorrect_signup_message_fname_text(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        fname_input = self.driver.find_element(By.ID, "firstName")
        fname_input.send_keys("Name")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        
        self.assertEqual(
            error_message.text, "User validation failed: lastName: Path `lastName` is required., email: Email is invalid, password: Path `password` is required."
        )

    def test_incorrect_signup_message_fl_name_displayed(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        fname_input = self.driver.find_element(By.ID, "firstName")
        fname_input.send_keys("Name")
        lname_input = self.driver.find_element(By.ID, "lastName")
        lname_input.send_keys("Last name")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        
        self.assertTrue(error_message.is_displayed())

    def test_incorrect_signup_message_fl_name_text(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        fname_input = self.driver.find_element(By.ID, "firstName")
        fname_input.send_keys("Name")
        lname_input = self.driver.find_element(By.ID, "lastName")
        lname_input.send_keys("Last name")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        
        self.assertEqual(
            error_message.text, "User validation failed: email: Email is invalid, password: Path `password` is required."
        )

    def test_incorrect_signup_message_email_displayed(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        fname_input = self.driver.find_element(By.ID, "firstName")
        fname_input.send_keys("Name")
        lname_input = self.driver.find_element(By.ID, "lastName")
        lname_input.send_keys("Last name")
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("example@email.com")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        
        self.assertTrue(error_message.is_displayed())

    def test_incorrect_signup_message_email_text(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        fname_input = self.driver.find_element(By.ID, "firstName")
        fname_input.send_keys("Name")
        lname_input = self.driver.find_element(By.ID, "lastName")
        lname_input.send_keys("Last name")
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("example@email.com")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        
        self.assertEqual(
            error_message.text, "User validation failed: password: Path `password` is required."
        )

    def test_incorrect_signup_message_wrong_email_displayed(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        fname_input = self.driver.find_element(By.ID, "firstName")
        fname_input.send_keys("Name")
        lname_input = self.driver.find_element(By.ID, "lastName")
        lname_input.send_keys("Last name")
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("exampleemail.com")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        
        self.assertTrue(error_message.is_displayed())

    def test_incorrect_signup_message_wrong_email_text(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        fname_input = self.driver.find_element(By.ID, "firstName")
        fname_input.send_keys("Name")
        lname_input = self.driver.find_element(By.ID, "lastName")
        lname_input.send_keys("Last name")
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("exampleemail.com")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        
        self.assertEqual(
            error_message.text, "User validation failed: email: Email is invalid, password: Path `password` is required."
        )

    def test_incorrect_signup_message_wrong_password_displayed(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        fname_input = self.driver.find_element(By.ID, "firstName")
        fname_input.send_keys("Name")
        lname_input = self.driver.find_element(By.ID, "lastName")
        lname_input.send_keys("Last name")
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("example@email.com")
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("1")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        
        self.assertTrue(error_message.is_displayed())

    def test_incorrect_signup_message_wrong_password_text(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        fname_input = self.driver.find_element(By.ID, "firstName")
        fname_input.send_keys("Name")
        lname_input = self.driver.find_element(By.ID, "lastName")
        lname_input.send_keys("Last name")
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("example@email.com")
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("1")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        
        self.assertEqual(
            error_message.text, "User validation failed: password: Path `password` (`1`) is shorter than the minimum allowed length (7)."
        )

    def test_correct_signup(self):
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
        fname_input = self.driver.find_element(By.ID, "firstName")
        fname_input.send_keys("Name")
        lname_input = self.driver.find_element(By.ID, "lastName")
        lname_input.send_keys("Last name")
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("example@email.com")
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("haslouzytkownika123@")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        current_url = self.driver.current_url
        response = requests.get(current_url)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
