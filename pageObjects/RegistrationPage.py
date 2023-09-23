from selenium.webdriver.common.by import By

from utilities.random_data import random_data_for_testcase


class RegistrationPage:

    # Locators information

    textbox_firstName_id = "customer.firstName"
    textbox_lastName_id = "customer.lastName"
    textbox_address_id = "customer.address.street"
    textbox_city_id = "customer.address.city"
    textbox_state_id = "customer.address.state"
    textbox_zipCode_id = "customer.address.zipCode"
    textbox_phone_id = "customer.phoneNumber"
    textbox_ssn_id = "customer.ssn"
    textbox_userName_id = "customer.username"
    textbox_password_id = "customer.password"
    textbox_confirmPassword_id = "repeatedPassword"
    btn_register_xpath = "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[13]/td[2]/input"

    # Datas for the registration page

    firstname = random_data_for_testcase.rnd_name(6)
    lastname = random_data_for_testcase.rnd_name(5)
    address = random_data_for_testcase.rnd_name(7)
    city = random_data_for_testcase.rnd_name(6)
    state = random_data_for_testcase.rnd_name(7)
    zipCode = random_data_for_testcase.rnd_number(6)
    phone = random_data_for_testcase.rnd_number(10)
    ssn = random_data_for_testcase.rnd_number(5)

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, FirstName):
        fname = self.driver.find_element(By.ID, self.textbox_firstName_id)
        fname.clear()
        fname.send_keys(FirstName)

    def setLastName(self, LastName):
        Lname = self.driver.find_element(By.ID, self.textbox_lastName_id)
        Lname.clear()
        Lname.send_keys(LastName)

    def setAddress(self, Address):
        add = self.driver.find_element(By.ID, self.textbox_address_id)
        add.clear()
        add.send_keys(Address)

    def setCity(self, City):
        cty = self.driver.find_element(By.ID, self.textbox_city_id)
        cty.clear()
        cty.send_keys(City)

    def setState(self, State):
        state = self.driver.find_element(By.ID, self.textbox_state_id)
        state.clear()
        state.send_keys(State)

    def setZipCode(self, Zipcode):
        zipcode = self.driver.find_element(By.ID, self.textbox_zipCode_id)
        zipcode.clear()
        zipcode.send_keys(Zipcode)

    def setPhone(self, Phone):
        number = self.driver.find_element(By.ID, self.textbox_phone_id)
        number.clear()
        number.send_keys(Phone)

    def setSSN(self, Ssn):
        sn = self.driver.find_element(By.ID, self.textbox_ssn_id)
        sn.clear()
        sn.send_keys(Ssn)

    def setUserName(self, UserName):
        uname = self.driver.find_element(By.ID, self.textbox_userName_id)
        uname.clear()
        uname.send_keys(UserName)

    def setPassword(self, Password):
        pwd = self.driver.find_element(By.ID, self.textbox_password_id)
        pwd.clear()
        pwd.send_keys(Password)

    def setConfirm(self, Confirm):
        cnf = self.driver.find_element(By.ID, self.textbox_confirmPassword_id)
        cnf.clear()
        cnf.send_keys(Confirm)

    def clickRegister(self):
        reg = self.driver.find_element(By.XPATH, self.btn_register_xpath)
        reg.click()

    def common_registration_method(self, username, password):
        self.setFirstName(self.firstname)
        self.setLastName(self.lastname)
        self.setAddress(self.address)
        self.setCity(self.city)
        self.setState(self.state)
        self.setZipCode(self.zipCode)
        self.setPhone(self.phone)
        self.setSSN(self.ssn)
        self.setUserName(username)
        self.setPassword(password)
        self.setConfirm(password)
        self.clickRegister()
