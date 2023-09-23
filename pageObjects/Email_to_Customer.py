from selenium.webdriver.common.by import By
from utilities.random_data import random_data_for_testcase


class Email_to_Customer:

    textbox_name_xpath = "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[1]/td[2]/input"
    textbox_email_xpath = "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[2]/td[2]/input"
    textbox_phone_xpath = "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[3]/td[2]/input"
    textbox_message_xpath = "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[4]/td[2]/textarea"
    btn_send_to_customer_care_xpath = "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[5]/td[2]/input"
    assertion_text_xpath = "/html/body/div[1]/div[3]/div[2]/p[2]"

    Name = random_data_for_testcase.rnd_name(6)
    Email = Name+"@gmail.com"
    Phone = random_data_for_testcase.rnd_number(10)
    Message = random_data_for_testcase.rnd_name(150)

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, Name):
        nm = self.driver.find_element(By.XPATH, self.textbox_name_xpath)
        nm.clear()
        nm.send_keys(Name)

    def set_email(self, Email):
        eml = self.driver.find_element(By.XPATH, self.textbox_email_xpath)
        eml.clear()
        eml.send_keys(Email)

    def set_phone(self, Phone):
        phn = self.driver.find_element(By.XPATH, self.textbox_phone_xpath)
        phn.clear()
        phn.send_keys(Phone)

    def set_message(self, Message):
        msg = self.driver.find_element(By.XPATH, self.textbox_message_xpath)
        msg.clear()
        msg.send_keys(Message)

    def click_sendToCustomerCare(self):
        send = self.driver.find_element(By.XPATH, self.btn_send_to_customer_care_xpath)
        send.click()

    """def send_Assertion_text(self):
        ass = self.driver.find_element(By.XPATH, self.assertion_text_xpath)
        return ass.text()"""

    def send_message(self):
        self.set_name(self.Name)
        self.set_email(self.Email)
        self.set_phone(self.Phone)
        self.set_message(self.Message)
        self.click_sendToCustomerCare()

