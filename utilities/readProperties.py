import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getApplicationMode():
        mode = config.get('common info', 'mode')
        return mode

    @staticmethod
    def getApplicationBrowser():
        brow = config.get('common info', 'browser')
        return brow

    """ @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
    """
