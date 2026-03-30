class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stringstack = []
        numstack = []
        currentstring = ""
        currentnum = 0

        for char in s:
            if char.isdigit():
                currentnum = currentnum * 10 + int(char)
            elif char == "[":
                stringstack.append(currentstring)
                numstack.append(currentnum)
                currentnum = 0
                currentstring = ""
            elif char == "]":
                num = numstack.pop()
                oldstring = stringstack.pop()
                currentstring = oldstring + num * currentstring
            else:
                currentstring += char

        return currentstring