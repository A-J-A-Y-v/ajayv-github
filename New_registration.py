from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Orange:

    def __init__(self):
        self.url = "https://demo.nopcommerce.com/"
        self.driver = webdriver.Chrome()
        self.register_user = '//a[@href="/register?returnUrl=%2F"]'
        self.gender = '//label[@class="forcheckbox" and @for="gender-male"]'
        self.firstname = "FirstName"
        self.lastname = "LastName"
        self.email = "Email"
        self.password = "Password"
        self.confirm_password = "ConfirmPassword"
        self.submit_button = '//button[@type="submit"]'

    def browse(self):
        self.driver.get(self.url)
        print(self.driver.title)
        self.driver.maximize_window()
        sleep(1)

    def nopcommerce(self):
        sleep(1)
        register_user_webelement = self.driver.find_element(By.XPATH, self.register_user)
        register_user_webelement.click()
        sleep(2)

        gender_webelement = self.driver.find_element(By.XPATH, self.gender)
        gender_webelement.click()
        sleep(2)

        firstname_webelement = self.driver.find_element(By.ID, self.firstname)
        firstname_webelement.send_keys("Ajay")

        lastname_webelement = self.driver.find_element(By.ID, self.lastname)
        lastname_webelement.send_keys("V")
        sleep(2)

        email_webelement = self.driver.find_element(By.ID, self.email)
        email_webelement.send_keys("vajay@gmail.com")
        sleep(2)

        password_webelement = self.driver.find_element(By.ID, self.password)
        password_webelement.send_keys("Welcome@123")
        sleep(2)

        confirm_password_webelement = self.driver.find_element(By.ID, self.confirm_password)
        confirm_password_webelement.send_keys("Welcome@123")
        sleep(2)

        submit_webelement = self.driver.find_element(By.XPATH, self.submit_button)
        submit_webelement.click()
        sleep(2)


obj = Orange()
obj.browse()
obj.nopcommerce()
sleep(2)
