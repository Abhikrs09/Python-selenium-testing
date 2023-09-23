import pytest

from pageObjects.Homepage import Homepage
from pageObjects.LoginPage import LoginPage
from pageObjects.RegistrationPage import RegistrationPage
from utilities.customLogger import LogGen
from utilities.random_data import random_data_for_testcase
from utilities.readProperties import ReadConfig


class Test_003_LoginInvalid_Credentials:
    baseUrl = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_with_invalid_credentials(self, setup):

        username = random_data_for_testcase.rnd_name(7)
        password = random_data_for_testcase.rnd_name(7)
        wrongPassword = "0000"

        self.logger.info("********************** Test_003_Login ************************")
        self.logger.info("********************** Verifying able to login using invalid credentials ************************")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.clickRegister()

        self.reg = RegistrationPage(self.driver)
        self.reg.common_registration_method(username, password)

        self.home = Homepage(self.driver)
        self.home.click_logOut_xpath()

        self.lp.common_login_method(username, wrongPassword)

        act_title = self.driver.title

        if act_title != "ParaBank | Customer Created":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_with_invalid_credentials.png")
            self.driver.close()
            self.logger.info("********************** Login Test Failed  ************************")
            assert True
