from selenium.webdriver.common.by import By


class NewAccountPage:

    btn_OpenNewAccount_xpath = "/html/body/div[1]/div[3]/div[2]/div/div/form/div/input"
    linktext_newAccountId_id = "newAccountId"

    def __init__(self, driver):
        self.driver = driver

    def click_OpenNewAccount_btn(self):
        openNewAccount = self.driver.find_element(By.XPATH, self.btn_OpenNewAccount_xpath)
        openNewAccount.click()

    def click_newAccountId_link(self):
        newAccId = self.driver.find_element(By.ID, self.linktext_newAccountId_id)
        newAccId.click()

