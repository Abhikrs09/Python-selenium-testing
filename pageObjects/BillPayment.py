
from selenium.webdriver.common.by import By
from utilities.random_data import random_data_for_testcase


class BillPayment:

    textbox_payeeName_name = "payee.name"
    textbox_address_name = "payee.address.street"
    textbox_city_name = "payee.address.city"
    textbox_state_name = "payee.address.state"
    textbox_zipCode_name = "payee.address.zipCode"
    textbox_phone_name = "payee.phoneNumber"
    textbox_account_name = "payee.accountNumber"
    textbox_verifyAccount_name = "payee.accountNumber"
    textbox_amount_name = "amount"
    btn_sendPayment_className = "button"

    PayeeName = random_data_for_testcase.rnd_name(6)
    Address = random_data_for_testcase.rnd_name(10)
    City = random_data_for_testcase.rnd_name(6)
    State = random_data_for_testcase.rnd_name(5)
    zipCode = random_data_for_testcase.rnd_number(6)
    Phone = random_data_for_testcase.rnd_number(10)
    Account = random_data_for_testcase.rnd_number(5)
    Amount = random_data_for_testcase.rnd_number(2)

    def __init__(self, driver):
        self.driver = driver

    def set_payeeName(self, PayeeName):
        payee = self.driver.find_element(By.NAME, self.textbox_payeeName_name)
        payee.clear()
        payee.send_keys(PayeeName)

    def set_Address(self, Address):
        add = self.driver.find_element(By.NAME, self.textbox_address_name)
        add.clear()
        add.send_keys(Address)

    def set_city(self, City):
        cty = self.driver.find_element(By.NAME, self.textbox_city_name)
        cty.clear()
        cty.send_keys(City)

    def set_State(self, State):
        st = self.driver.find_element(By.NAME, self.textbox_state_name)
        st.clear()
        st.send_keys(State)

    def set_zipCode(self, zipCode):
        zipC = self.driver.find_element(By.NAME, self.textbox_zipCode_name)
        zipC.clear()
        zipC.send_keys(zipCode)

    def set_Phone(self, Phone):
        pn = self.driver.find_element(By.NAME,  self.textbox_phone_name)
        pn.clear()
        pn.send_keys(Phone)

    def set_Account(self, Account):
        zipC = self.driver.find_element(By.NAME, self.textbox_account_name)
        zipC.clear()
        zipC.send_keys(Account)

    def set_VerifyAccount(self, Account):
        zipC = self.driver.find_element(By.NAME, self.textbox_verifyAccount_name)
        zipC.clear()
        zipC.send_keys(Account)

    def set_Amount(self, Amount):
        zipC = self.driver.find_element(By.NAME, self.textbox_amount_name)
        zipC.clear()
        zipC.send_keys(Amount)

    def click_sendPayment_className(self):
        send = self.driver.find_element(By.CLASS_NAME, self.btn_sendPayment_className)
        send.click()

    def bill_payment(self):
        self.set_payeeName(self.PayeeName)
        self.set_Address(self.Address)
        self.set_city(self.City)
        self.set_State(self.State)
        self.set_zipCode(self.zipCode)
        self.set_Phone(self.Phone)
        self.set_Account(self.Account)
        self.set_VerifyAccount(self.Account)
        self.set_Amount(self.Amount)
        self.click_sendPayment_className()

