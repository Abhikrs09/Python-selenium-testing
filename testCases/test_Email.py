import pytest

from pageObjects.Homepage import Homepage
from pageObjects.LoginPage import LoginPage
from pageObjects.RegistrationPage import RegistrationPage
from pageObjects.Email_to_Customer import Email_to_Customer
from utilities.customLogger import LogGen
from utilities.random_data import random_data_for_testcase
from utilities.readProperties import ReadConfig


class Test_004_email:
    baseUrl = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_email_to_customer_care(self, setup):

        username = random_data_for_testcase.rnd_name(7)
        password = random_data_for_testcase.rnd_name(7)

        self.driver = setup
        # self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.clickRegister()

        self.reg = RegistrationPage(self.driver)
        self.reg.common_registration_method(username, password)

        self.home = Homepage(self.driver)
        self.home.click_email_xpath()

        self.eml = Email_to_Customer(self.driver)
        self.eml.send_message()

        act_title = self.driver.title

        if act_title == "ParaBank | Customer Care":
            assert True
            self.driver.close()
            self.logger.info("********************** Email has been send ************************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_email_to_customer_care.png")
            self.driver.close()
            self.logger.info("********************** Email has not send ************************")
            assert False

    @pytest.mark.sanity
    def test_Logout(self,setup):
        username = random_data_for_testcase.rnd_name(7)
        password = random_data_for_testcase.rnd_name(7)

        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.clickRegister()

        self.reg = RegistrationPage(self.driver)
        self.reg.common_registration_method(username, password)

        self.home = Homepage(self.driver)
        self.home.click_logOut_xpath()

        act_title = self.driver.title + "123"

        if act_title == "ParaBank | Welcome | Online Banking":
            assert True
            self.driver.close()
            self.logger.info("********************** Logout Successfully ************************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_email_to_customer_care.png")
            self.driver.close()
            self.logger.info("********************** Unable to Logout ************************")
            assert False


