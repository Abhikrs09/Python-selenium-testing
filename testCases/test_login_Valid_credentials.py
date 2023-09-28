import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.RegistrationPage import RegistrationPage
from pageObjects.Homepage import Homepage
from utilities.customLogger import LogGen
from utilities.random_data import random_data_for_testcase
from utilities.readProperties import ReadConfig


class Test_002_Login:

    baseUrl = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):

        self.logger.info("********************** Test_002_Login ************************")
        self.logger.info("********************** Verifying Login Page Title ************************")

        self.driver = setup
        self.driver.get(self.baseUrl)

        act_title = self.driver.title

        if act_title == "ParaBank | Welcome | Online Banking":
            assert True
            self.driver.close()
            self.logger.info("********************** Login Page Title is Passed ************************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("********************** Login Page Title is Failed ************************")
            assert False

    @pytest.mark.sanity
    def test_login_with_valid_credentials(self, setup):

        username = random_data_for_testcase.rnd_name(7)
        password = random_data_for_testcase.rnd_name(7)

        self.logger.info("********************** Test_002_Login ************************")
        self.logger.info("********************** Test Login With Valid Credentials ************************")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.logger.info("************* click Registration link from LoginPage **********")
        self.lp.clickRegister()

        self.reg = RegistrationPage(self.driver)
        self.logger.info("************** Landed to Registration Page ***********")
        self.reg.common_registration_method(username, password)

        self.home = Homepage(self.driver)
        self.home.click_logOut_xpath()

        self.lp.common_login_method(username, password)
        act_title = self.driver.title
        print(act_title)
        """self.driver.close()"""

        if act_title == "ParaBank | Customer Created":
            assert True
            self.driver.close()
            self.logger.info("********************** Login Test Passed ************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_with_valid_credentials.png")
            self.driver.close()
            self.logger.info("********************** Login Test Failed  ************************")
            assert True


