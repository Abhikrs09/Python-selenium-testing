from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_name = "username"
    textbox_password_name = "password"
    btn_login_class = "button"
    link_register_linkText = "Register"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        userN = self.driver.find_element(By.NAME, self.textbox_username_name)
        userN.clear()
        userN.send_keys(username)

    def setPass(self, password):
        passW = self.driver.find_element(By.NAME, self.textbox_password_name)
        passW.clear()
        passW.send_keys(password)

    def clickLogin(self):
        loginKey = self.driver.find_element(By.CLASS_NAME, self.btn_login_class)
        loginKey.click()

    def clickRegister(self):
        regKey = self.driver.find_element(By.LINK_TEXT, self.link_register_linkText)
        regKey.click()

    def common_login_method(self, username, password):
        self.setUserName(username)
        self.setPass(password)
        self.clickLogin()

