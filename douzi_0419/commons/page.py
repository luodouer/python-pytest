# encoding=utf-8
# @Author   ： 豆子
# @Function ：

import random
import string


class RandomChoice:
    @staticmethod
    def random_choice_one(min, max):
        rand_data = random.randint(min, max)
        return rand_data

    @staticmethod
    def random_more_str(num):
        salt = ''.join(random.sample(string.ascii_letters + string.digits, num))
        # salt = ''.join(random.sample(string.digits, num))
        return salt


if __name__ == '__main__':
    print(RandomChoice.random_more_str(6))