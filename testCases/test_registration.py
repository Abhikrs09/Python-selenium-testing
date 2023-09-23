import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.RegistrationPage import RegistrationPage
from utilities.customLogger import LogGen
from utilities.random_data import random_data_for_testcase
from utilities.readProperties import ReadConfig


class Test_001_Registration:

    logger = LogGen.loggen()

    username = random_data_for_testcase.rnd_name(7)
    password = random_data_for_testcase.rnd_name(7)

    @pytest.mark.regression
    def test_Registration(self, setup):
        self.logger.info("************* Test_001_Registration**************")
        self.logger.info("********************** Verifying The Registration Page ************************")

        self.driver = setup
        self.driver.get(ReadConfig.getApplicationUrl())
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.logger.info("************* click Registration link from LoginPage **********")
        self.lp.clickRegister()

        self.logger.info("************** Landed to Registration Page ***********")
        self.reg = RegistrationPage(self.driver)

        self.logger.info("************** Inserting User Details ***********")
        self.reg.common_registration_method(self.username, self.password)
        self.logger.info("****************** click on Register Button **********")

        act_title = self.driver.title
        if act_title == "ParaBank | Customer Created":
            assert True
            self.driver.close()
            self.logger.info("********************** Registration Test Passed ************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_registration.png")
            self.driver.close()
            self.logger.info("********************** Registration Test Failed  ************************")
            assert False
