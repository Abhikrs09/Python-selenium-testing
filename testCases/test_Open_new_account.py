import time

import pytest

from pageObjects.Homepage import Homepage
from pageObjects.LoginPage import LoginPage
from pageObjects.NewAccountPage import NewAccountPage
from pageObjects.RegistrationPage import RegistrationPage
from utilities.customLogger import LogGen
from utilities.random_data import random_data_for_testcase
from utilities.readProperties import ReadConfig


class Test_004_new_Account:

    baseUrl = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_new_Account_creation(self, setup):

        username = random_data_for_testcase.rnd_name(7)
        password = random_data_for_testcase.rnd_name(7)

        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.clickRegister()

        self.reg = RegistrationPage(self.driver)
        self.reg.common_registration_method(username, password)
        time.sleep(3)
        self.home = Homepage(self.driver)
        self.home.click_newAccount_xpath()
        time.sleep(3)
        self.newAcc = NewAccountPage(self.driver)
        self.newAcc.click_OpenNewAccount_btn()
        time.sleep(3)
        self.newAcc.click_newAccountId_link()
        time.sleep(3)
        act_title = self.driver.title

        if act_title == "ParaBank | Account Activity":
            assert True
            self.driver.close()
            self.logger.info("********************** Account is Created ************************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_new_Account_creation.png")
            self.driver.close()
            self.logger.info("********************** Account is not Created ************************")
            assert False


