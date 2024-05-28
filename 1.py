# import re
# text = input()
# print(re.split(' |,|:|\.',text))
#

def is_prime(n):
    """判断素数的函数,接收一个正整数为参数，参数是素数时返回True，否则返回False"""
    # =======================================================
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        else:
            return True


# =======================================================


def goldbach_conjecture(num):
    """ 哥德巴赫猜想, 接收一个不小于4的正整数为参数。
    当参数为不小于4的偶数时，将其分解为两个素数的加和，按小数+数的格式输出。
    有多种组合时全部输出，但不输出重复的组合，例如输出8=3+5，不输出8=5+3。
    参数为奇数或小于4时，输出'Data error!'
    """

    # =======================================================


    if num >= 4 and num%2==0:
            for i in range(2, num//2+1):
                if is_prime(i) and is_prime(num - i):
                    print("{}={}+{}".format(num,i,num-i))
    else:
        print("Data error!")
    # =======================================================


if __name__ == '__main__':
    positive_even = int(input())  # 输入一个正数
    goldbach_conjecture(positive_even)