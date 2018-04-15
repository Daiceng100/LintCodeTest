# coding=utf-8
class Solution:
    """
    @param character: a character
    @return: a character
    """
    def lowercaseToUppercase(self, character):
        return chr(ord(character) - 32)


if __name__ == '__main__':
    b = Solution().lowercaseToUppercase('a')
    print(b)