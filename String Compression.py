class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read = 0
        write = 0
        while read < len(chars):
            count = 0
            currentcharacter = chars[read]
            while read < len(chars) and chars[read] == currentcharacter:
                read += 1
                count += 1
            chars[write] = currentcharacter
            write += 1
            if count > 1:
                countstring = str(count)
                for i in range(len(countstring)):
                    chars[write] = countstring[i]
                    write += 1
                
        return write