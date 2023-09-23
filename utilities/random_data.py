import random
import string


class random_data_for_testcase:

    @staticmethod
    def rnd_name(length):
        result_str = "".join(random.choice(string.ascii_letters) for i in range(length))
        return result_str

    @staticmethod
    def rnd_number(length):
        mini = pow(10, length-1)
        maxi = pow(10, length)-1
        return random.randint(mini, maxi)

