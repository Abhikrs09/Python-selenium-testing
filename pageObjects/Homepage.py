from selenium.webdriver.common.by import By


class Homepage:
    link_newAccount_xpath = "/html/body/div[1]/div[3]/div[1]/ul/li[1]/a"
    link_bill_Pay_xpath = "/html/body/div[1]/div[3]/div[1]/ul/li[4]/a"
    link_email_xpath = "/html/body/div[1]/div[2]/ul[2]/li[3]/a"
    link_logOut_xpath = "/html/body/div[1]/div[3]/div[1]/ul/li[8]/a"

    def __init__(self, driver):
        self.driver = driver

    def click_newAccount_xpath(self):
        new_acc = self.driver.find_element(By.XPATH, self.link_newAccount_xpath)
        new_acc.click()

    def click_billPay_xpath(self):
        bill_pay = self.driver.find_element(By.XPATH, self.link_bill_Pay_xpath)
        bill_pay.click()

    def click_email_xpath(self):
        email = self.driver.find_element(By.XPATH, self.link_email_xpath)
        email.click()

    def click_logOut_xpath(self):
        log_out = self.driver.find_element(By.XPATH, self.link_logOut_xpath)
        log_out.click()
