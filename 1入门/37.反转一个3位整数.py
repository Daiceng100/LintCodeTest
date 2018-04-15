# coding=utf-8
class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        a = []
        sum = 0
        while(number != 0):
            temp = number % 10
            number //= 10
            a.append(temp)

        for x in a:
            sum = sum * 10 + x

        return sum


if __name__ == '__main__':
    b = Solution().reverseInteger(900)
    print(b)