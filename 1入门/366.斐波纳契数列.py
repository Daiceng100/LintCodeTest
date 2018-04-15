# coding=utf-8
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        # i = 2
        # x = 0
        # y = 1
        # if (n == 1):
        #     return x
        # elif (n == 2):
        #     return y
        # else:
        #     while(i < n):
        #             x, y = y, x+y
        #             i +=1
        #     return y

        a = 0
        b = 1
        for i in range(n - 1):
            a, b = b, a+b
        return a

if __name__ == '__main__':
    c = Solution().fibonacci(1)
    print(c)
