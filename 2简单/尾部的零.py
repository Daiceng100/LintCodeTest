# coding=utf-8
class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        result = 0
        temp = n // 5
        while temp != 0:
            result += temp
            temp //= 5
        return result


if __name__ == '__main__':
    a = Solution().trailingZeros(1000)
    print(a)
