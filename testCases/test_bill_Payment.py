import pytest

from pageObjects.BillPayment import BillPayment
from pageObjects.Homepage import Homepage
from pageObjects.LoginPage import LoginPage
from pageObjects.RegistrationPage import RegistrationPage
from utilities.customLogger import LogGen
from utilities.random_data import random_data_for_testcase
from utilities.readProperties import ReadConfig


class Test_004_bill_payment:
    baseUrl = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_bill_payment(self, setup):

        username = random_data_for_testcase.rnd_name(7)
        password = random_data_for_testcase.rnd_name(7)

        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.clickRegister()

        self.reg = RegistrationPage(self.driver)
        self.reg.common_registration_method(username, password)

        self.home = Homepage(self.driver)
        self.home.click_billPay_xpath()

        self.bill = BillPayment(self.driver)
        self.bill.bill_payment()

        act_title = self.driver.title
        print(act_title)

        if act_title == "ParaBank | About Us":
            assert True
            self.driver.close()
            self.logger.info("********************** Bill payment Successful ************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_bill_payment.png")
            self.driver.close()
            self.logger.info("********************** Bill payment Failed ************************")
            assert False
